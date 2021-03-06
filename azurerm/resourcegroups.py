'''resourcegroups.py - azurerm functions for Resource Groups.'''
import json
from .restfns import do_delete, do_get, do_put
from .settings import get_rm_endpoint, BASE_API


def create_resource_group(access_token, subscription_id, rgname, location):
    '''Create a resource group in the specified location.

    Args:
        access_token (str): A valid Azure authentication token.
        subscription_id (str): Azure subscription id.
        rgname (str): Azure resource group name.
        location (str): Azure data center location. E.g. westus.

    Returns:
        HTTP response. JSON body.
    '''
    endpoint = ''.join([get_rm_endpoint(),
                        '/subscriptions/', subscription_id,
                        '/resourcegroups/', rgname,
                        '?api-version=', BASE_API])
    rg_body = {'location': location}
    body = json.dumps(rg_body)
    return do_put(endpoint, body, access_token)


def delete_resource_group(access_token, subscription_id, rgname):
    '''Delete the named resource group.

    Args:
        access_token (str): A valid Azure authentication token.
        subscription_id (str): Azure subscription id.
        rgname (str): Azure resource group name.

    Returns:
        HTTP response.
    '''
    endpoint = ''.join([get_rm_endpoint(),
                        '/subscriptions/', subscription_id,
                        '/resourcegroups/', rgname,
                        '?api-version=', BASE_API])
    return do_delete(endpoint, access_token)


def get_resource_group(access_token, subscription_id, rgname):
    '''Get details about the named resource group.

    Args:
        access_token (str): A valid Azure authentication token.
        subscription_id (str): Azure subscription id.
        rgname (str): Azure resource group name.

    Returns:
        HTTP response.
    '''
    endpoint = ''.join([get_rm_endpoint(),
                        '/subscriptions/', subscription_id,
                        '/resourceGroups/', rgname,
                        '?api-version=', BASE_API])
    return do_get(endpoint, access_token)


def list_resource_groups(access_token, subscription_id):
    '''List the resource groups in a subscription.

    Args:
        access_token (str): A valid Azure authentication token.
        subscription_id (str): Azure subscription id.

    Returns:
        HTTP response.
    '''
    endpoint = ''.join([get_rm_endpoint(),
                        '/subscriptions/', subscription_id,
                        '/resourceGroups/',
                        '?api-version=', BASE_API])
    return do_get(endpoint, access_token)
