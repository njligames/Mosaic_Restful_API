import connexion
import six

from swagger_server.models.process import Process  # noqa: E501
from swagger_server import util


def delete_order(processId):  # noqa: E501
    """Delete past process by ID

    For valid response try integer IDs with positive integer value.         Negative or non-integer values will generate API errors # noqa: E501

    :param processId: ID of the order that needs to be deleted
    :type processId: int

    :rtype: None
    """
    return 'do some magic!'


def get_order_by_id(processId):  # noqa: E501
    """Find past processes by ID

    For valid response try integer IDs with value &gt;&#x3D; 1 and &lt;&#x3D; 10.         Other values will generated exceptions # noqa: E501

    :param processId: ID of targetImage that needs to be fetched
    :type processId: int

    :rtype: Process
    """
    return 'do some magic!'


def place_order(body):  # noqa: E501
    """Place a process order for a Mosaic Image

     # noqa: E501

    :param body: order placed for processing the targetImage
    :type body: dict | bytes

    :rtype: Process
    """
    if connexion.request.is_json:
        body = Process.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
