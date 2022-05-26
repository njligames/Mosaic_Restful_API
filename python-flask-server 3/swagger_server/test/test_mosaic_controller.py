# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.process import Process  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMosaicController(BaseTestCase):
    """MosaicController integration test stubs"""

    def test_delete_order(self):
        """Test case for delete_order

        Delete past process by ID
        """
        response = self.client.open(
            '/v2/mosaic/process/{processId}'.format(processId=2),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_order_by_id(self):
        """Test case for get_order_by_id

        Find past processes by ID
        """
        response = self.client.open(
            '/v2/mosaic/process/{processId}'.format(processId=10),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_place_order(self):
        """Test case for place_order

        Place a process order for a Mosaic Image
        """
        body = Process()
        response = self.client.open(
            '/v2/mosaic/process',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
