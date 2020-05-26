import unittest

from flask import json

from backend.app import create_app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

    def tearDown(self):
        pass

    def test_get_map(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(data['data'], 'A map is here')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_survey(self):
        res = self.client().get('/survey')
        data = json.loads(res.data)

        self.assertEqual(data['data'], 'Survey form is here')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_post_survey(self):
        # bad request call
        res = self.client().post('/survey')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['name'], 'Bad Request')

        # successful call
        # TODO fill out when known
        request_data = json.dumps({
            'country_region_code': None,
            'country_region': None,
            'sub_region_1': None,
            'sub_region_2': None,
            'date': None,
            'still_on_lockdown': False
        })

        res = self.client().post('/survey', data=request_data)
        data = json.loads(res.data)

        self.assertEqual(data['prediction'], 0.0)
        self.assertEqual(data['message'], '')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

if __name__ == '__main__':
    unittest.main()
