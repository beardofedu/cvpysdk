#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------
# Copyright ©2016 Commvault Systems, Inc.
# See LICENSE.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""File for operating on a Virtual Server Instance.

VirualServerInstance is the only class defined in this file.

VirtualServerInstance: Derived class from Instance Base class, representing a
                            virtual server instance, and to perform operations on that instance

VirtualServerInstance:

     __new__                    --  Decides which instance object needs to be created

    __init__                    --  initialise object of vsinstance class associated with
                                            the specified agent, instance name and instance id
    

    _get_instance_properties()  --  Instance class method overwritten to add virtual server
                                        instance properties as well

    associated_clients                --  getter or setter for the associated clients

    co_ordinator                    --  getter 


"""

from __future__ import unicode_literals

from ..instance import Instance
from ..client import Client
from ..exception import SDKException
from .. import constants



class VirtualServerInstance(Instance):
    """Class for representing an Instance of the Virtual Server agent."""

    def __new__(cls,agent_object, instance_name, instance_id=None):
        """Decides which instance object needs to be created"""
        
        hv_type = constants.hypervisor_type
        if(instance_name == hv_type.VIRTUAL_CENTER.value.lower()):
            from .virtualserver.VMwareInstance import VMwareInstance
            return object.__new__(VMwareInstance)
        
        elif(instance_name  == hv_type.MS_VIRTUAL_SERVER.value.lower()):
            from .virtualserver.hypervinstance import HyperVInstance
            return object.__new__(HyperVInstance)
        
        elif(instance_name  == hv_type.AMAZON.value.lower()):
            from .virtualserver.amazoninstance import AmazonInstance
            return object.__new__(AmazonInstance)
        
        elif(instance_name  == hv_type.AZURE.value.lower()):
            from .virtualserver.azureinstance import AzureInstance
            return object.__new__(AzureInstance)
        
        elif(instance_name  == hv_type.AZURE_V2.value.lower()):
            from .virtualserver.azureRMinstance import AzureRMInstance
            return object.__new__(AzureRMInstance)
        
    def _get_instance_properties(self):
        """Gets the properties of this instance.

            Raises:
                SDKException:
                    if response is empty
                    if response is not success
        """
        super(VirtualServerInstance, self)._get_instance_properties()

        self._vsinstancetype = None
        self._asscociatedclients = None
        if 'virtualServerInstance' in self._properties:
            self._virtualserverinstance  = self._properties["virtualServerInstance"]
            self._vsinstancetype = self._virtualserverinstance['vsInstanceType']
            self._asscociatedclients = self._virtualserverinstance['associatedClients']
    
        
    @property
    def associated_clients(self):
        """Treats the clients associated to this instance as a read-only attribute."""
        self._associated_clients = []
        if "memberServers" in self._asscociatedclients:       
            for client in self._asscociatedclients["memberServers"]:
                self._associated_clients.append(client["client"]["clientName"])
            return self._associated_clients
    
    @associated_clients.setter
    def associated_clients(self,clients_list):
        """sets the associated clients with Client Dict Provided as input
            
            it replaces the list of proxies in the GUI
        
        Args:
                client_list:    (list)       --- list of clients or client groups
        
        Raises:
            SDKException:
                if response is not success
                
                if input is not list of strings
                
                if input is not client of CS
                
                
        """
        for client_name in clients_list:
            if not isinstance(client_name, str):                
                raise SDKException('Instance', '105')
        
        client_json_list = []
        
        associatedClients = {
                    "memberServers":client_json_list
                }
        
        for client_name in clients_list:
            client_json = {
                "clientName": client_name
            }
            
            client_group_json = {
                "clientGroupName": client_name
            }
            
            common_json = {
                "srmReportSet": 0,
                "type": 0,
                "srmReportType": 0,
                "clientSidePackage": True,
                "_type_": 28,
                "consumeLicense": True
            }
            final_json = {}
            if self._commcell_object.clients.has_client(client_name):
                common_json['clientName'] = client_name
                final_json['client'] = common_json
            elif self._commcell_object.client_groups.has_clientgroup(client_name):
                common_json['clientName'] = client_name
                final_json['client'] = common_json
            else:
                raise SDKException('Instance', '105')
            
            client_json_list.append(final_json)
            
        associatedClients = {
                    "memberServers": client_json_list
                }
        self._set_instance_properties("_virtualserverinstance['associatedClients']", associatedClients)
       
 
    @property
    def co_ordinator(self):
        """Returns the Co_ordinator of this instance it is read-only attribute"""
        _associated_clients = self.associated_clients
        return _associated_clients['Clients'][0]
    
    def _get_instance_properties_json(self):
        """get the all instances related properties of the instances for which the json is same.
        
           eg. amazon and azure have similar structure
           
           Returns:
                dict - all instance properties put inside a dict
           
        """
        instance_json = {
                            "instanceProperties":
                                {
                                    "isDeleted": False,
                                    "instance": self._instance,
                                    "instanceActivityControl": self._instanceActivityControl,
                                    "virtualServerInstance": {
                                        "vsInstanceType": self._virtualserverinstance['vsInstanceType'],
                                        "associatedClients": self._virtualserverinstance['associatedClients'],
                                
                                    }
                                }
                        }
        return instance_json
    
    
    
   