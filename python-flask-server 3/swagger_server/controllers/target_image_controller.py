import connexion
import six

from swagger_server.models.target_image import TargetImage  # noqa: E501
from swagger_server import util


def add_pet(body):  # noqa: E501
    """Add a new Target Image to be processed as a mosaic

     # noqa: E501

    :param body: TargetImage object that needs to be added to be processed into a mosaic
    :type body: dict | bytes

    :rtype: TargetImage
    """
    if connexion.request.is_json:
        body = TargetImage.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_pet(targetImageId, api_key=None):  # noqa: E501
    """Deletes a Target Image

     # noqa: E501

    :param targetImageId: TargetImage id to delete
    :type targetImageId: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def find_pets_by_tags(tags):  # noqa: E501
    """Finds Target Image by tags

    Muliple tags can be provided with comma separated strings. Use         tag1, tag2, tag3 for testing. # noqa: E501

    :param tags: Tags to filter by
    :type tags: List[str]

    :rtype: List[TargetImage]
    """
    return 'do some magic!'


def get_pet_by_id(targetImageId):  # noqa: E501
    """Find Target Image by ID

    Returns a single targetImage # noqa: E501

    :param targetImageId: ID of targetImage to return
    :type targetImageId: int

    :rtype: TargetImage
    """
    return 'do some magic!'


def update_pet(body):  # noqa: E501
    """Update an existing Target Image

     # noqa: E501

    :param body: TargetImage object that needs to be added to be processed as a mosaic.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TargetImage.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
