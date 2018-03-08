# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------
# Copyright Commvault Systems, Inc.
# See LICENSE.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""File for handling all the exceptions for the CVPySDK python package.

EXCEPTION_DICT:
    A python dictionary for holding all the exception messages for a specific event or class.

    Any exceptions to be raised from the SDK in a module should be added to this dictionary.

    where,

        -   the key is the module name or the class name where the exception is raised

        -   the value is a dictionary:

            -   key is a unique ID to identify the exception message

            -   value is the exception message

|

SDKException:
    Class inheriting the "Exception" Base class for raising
    a specific exception for the CVPySDK python package.

    The user should create an instance of the SDKException class:

        **SDKException(exception_module, exception_id, exception_message)**

        where,

            -   exception_module:   the module in which the exception is being raised

                -   key in the EXCEPTION_DICT

            -   exception_id:       unique ID which identifies the message for the Exception

            -   exception_message:  additional message to the exception

                -   only applicable if the user wishes to provide an additional message to the
                    exception along with the message already present as the value for the
                    exception_module - exception_id pair

    Example:

        **raise SDKException('CVPySDK', '101')**

        will raise the exception as:

            SDKException: Failed to Login with the credentials provided

        and, **raise SDKException('CVPySDK', '101', 'Please check the credentials')**

        will raise:

            SDKException: Failed to Login with the credentials provided

            Please check the credentials

        where the user given message is appended to the original message joined by new line

"""

from __future__ import absolute_import
from __future__ import unicode_literals

# Common dictionary for all exceptions among the python package
EXCEPTION_DICT = {
    'Response': {
        '101': 'Response was not success',
        '102': 'Response received is empty'
    },
    'Commcell': {
        '101': 'Commcell is not reachable. Please check the commcell name and services again',
        '102': 'Authtoken not received. Please try again.',
        '103': 'Failed to get the CommServ details',
        '104': 'Failed to send an email to specified user'
    },
    'CVPySDK': {
        '101': 'Failed to Login with the credentials provided',
        '102': '',
        '103': 'Reached the maximum attempts limit',
        '104': 'This session has expired. Please login again',
        '105': 'Script Type is not valid'
    },
    'Client': {
        '101': 'Data type of the input(s) is not valid',
        '102': '',
        '103': 'Time Value should be greater than current time',
        '104': 'Time Value entered is not of correct format',
        '105': 'Script Type is not supported',
        '106': 'Failed to get the instance',
        '107': 'Service Restart timed out'
    },
    'Agent': {
        '101': 'Data type of the input(s) is not valid',
        '102': '',
        '103': 'Time Value should be greater than current time',
        '104': 'Time Value entered is not of correct format'
    },
    'Backupset': {
        '101': 'Data type of the input(s) is not valid',
        '102': '',
    },
    'Instance': {
        '101': 'Data type of the input(s) is not valid',
        '102': '',
        '103': 'Input date is incorrect',
        '104': 'Instance Level Browse is not supported. Instance should have a single backupset'
    },
    'Subclient': {
        '101': 'Data type of the input(s) is not valid',
        '102': '',
        '103': 'Backup Level not identified. Please check the backup level again',
        '104': 'File/Folder(s) to restore list is empty',
        '105': 'Type of client should either be the Client class instance or string',
        '106': 'Input date is incorrect',
        '107': 'End Date should be greater than the Start Date',
        '108': 'Time Value should be greater than current time',
        '109': 'Time Value entered is not of correct format',
        '110': 'No data found at the path specified',
        '111': 'No File/Folder matched the input value',
        '112': 'Method Not Implemented',
        '113': 'Type of instance should either be the Instance class instance or string',
        '114': 'Type of backupset should either be the Backupset class instance or string'
    },
    'Job': {
        '101': 'Incorrect JobId',
        '102': '',
        '103': 'No job exists with the specified Job ID',
        '104': 'No records found for this Job'
    },
    'Storage': {
        '101': 'Data type of the input(s) is not valid',
        '102': '',
        '103': 'Type of media agent should either be the MediaAgent class instance or string',
        '104': 'Type of library should either be the DiskLibrary class instance or string',
        '105': 'No storage policies exist for this user'
    },
    'Schedules': {
        '101': 'Invalid Class object passed as argument to the Schedules class',
        '102': 'Data type of the input(s) is not valid'
    },
    'ClientGroup': {
        '101': 'Data type of the input(s) is not valid',
        '102': '',
        '103': 'Time Value should be greater than current time',
        '104': 'Time Value entered is not of correct format'
    },
    'UserGroup': {
        '101': 'Data type of the input(s) is not valid',
        '102': ''
    },
    'Domain': {
        '101': 'Data type of the input(s) is not valid',
        '102': ''
    },
    'Alert': {
        '101': 'Data type of the input(s) is not valid',
        '102': ''
    },
    'Workflow': {
        '101': 'Data type of the input(s) is not valid',
        '102': '',
        '103': 'Input is not valid XML / file path',
        '104': 'No Workflow exists with the given name'
    },
    'Datacube': {
        '101': 'Data type of the input(s) is not valid',
        '102': '',
        '103': 'Failed to get the list of analytics engines',
        '104': 'Failed to get the datasources'
    },
    'GlobalFilter': {
        '101': 'Data type of the input(s) is not valid',
        '102': ''
    },
    'Plan': {
        '101': 'Data type of the input(s) is not valid',
        '102': ''
    },
    'Salesforce': {
        '101': 'Neither Sync Database enabled nor user provided database details for restore',
        '102': ''
    },
    'Metrics': {
        '101': 'Invalid input(s) specified'
    },
    'InternetOptions': {
        '101': 'Invalid input(s) specified'
    },
    'Virtual Machine': {
        '101': 'Data type of the input(s) is not valid',
        '102': ''
    },
    'User': {
        '101': 'Data type of input(s) is not valid',
        '102': ''
    },
    'Security': {
        '101': 'Data type of input(s) is not valid',
        '102': ''
    },
    'DownloadCenter': {
        '101': 'Response received is not a proper XML. Please check the XML',
        '102': '',
        '103': 'Category does not exist at Download Center',
        '104': 'Category already exists at Download Center',
        '105': 'Sub Category already exists for the given Category at Download Center',
        '106': 'Package does not exist at Download Center. Please check the name again',
        '107': 'Failed to download the package',
        '108': 'Category does not exists at Download Center',
        '109': 'Sub Category does not exists at Download Center',
        '110': 'Multiple platforms available. Please specify the platform',
        '111': ('Multiple download types available for this platform. '
                'Please specify the download type'),
        '112': 'Package is not available for the given platform',
        '113': 'Package is not available for the given download type',
        '114': 'Package already exists with the given name',
        '115': 'Version is not available on Download Center',
        '116': 'Platform is not supported on Download Center',
        '117': 'Download Type is not supported on Download Center',
        '118': 'File is not a valid README file',
        '119': 'Failed to upload the package'
    },
    'Organization': {
        '101': 'Data type of the input(s) is not valid',
        '102': '',
        '103': 'No organization exists with the given name',
        '104': 'Failed to delete the organization',
        '105': 'Email address is not valid',
        '106': 'Organization already exists',
        '107': 'Failed to add organization',
        '108': 'Failed to enable Auth Code Generation for the Organization',
        '109': 'Failed to disable Auth Code Generation for the Organization',
        '110': 'Failed to update the properties of the Organization',
        '111': ('Plan is not associated with the organization. '
                'Add plan to the Organization, and then set it as the default')
    },
    'StoragePool': {
        '101': 'Data type of the input(s) is not valid',
        '102': '',
        '103': 'No storage pool exists with the given name',
    },
    'Monitoring': {
        '101': 'Data type of the input(s) is not valid',
        '102': ''
    }
}


class SDKException(Exception):
    """Exception class for raising exception specific to a module."""

    def __init__(self, exception_module, exception_id, exception_message=""):
        """Initialize the SDKException class instance for the exception.

            Args:
                exception_module  (str)  --  name of the module where the exception was raised

                exception_id      (str)  --  id of the exception specific to the exception_module

                exception_message (str)  --  additional message about the exception

            Returns:
                object  -   instance of the SDKException class of type Exception

        """
        self.exception_module = exception_module
        self.exception_id = exception_id
        self.exception_message = EXCEPTION_DICT[exception_module][exception_id]

        if exception_message:
            if self.exception_message:
                self.exception_message = '\n'.join([self.exception_message, exception_message])
            else:
                self.exception_message = exception_message

        Exception.__init__(self, self.exception_message)
