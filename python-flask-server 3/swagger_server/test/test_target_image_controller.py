# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.target_image import TargetImage  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTargetImageController(BaseTestCase):
    """TargetImageController integration test stubs"""

    def test_add_pet(self):
        """Test case for add_pet

        Add a new Target Image to be processed as a mosaic
        """
        body = TargetImage()
        response = self.client.open(
            '/v2/targetImage',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_pet(self):
        """Test case for delete_pet

        Deletes a Target Image
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/v2/targetImage/{targetImageId}'.format(targetImageId=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_pets_by_tags(self):
        """Test case for find_pets_by_tags

        Finds Target Image by tags
        """
        query_string = [('tags', 'tags_example')]
        response = self.client.open(
            '/v2/targetImage/findByTags',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pet_by_id(self):
        """Test case for get_pet_by_id

        Find Target Image by ID
        """
        response = self.client.open(
            '/v2/targetImage/{targetImageId}'.format(targetImageId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pet(self):
        """Test case for update_pet

        Update an existing Target Image
        """
        body = TargetImage()
        response = self.client.open(
            '/v2/targetImage',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
