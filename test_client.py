import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from client import create_presence_message, parse_response

class TestClass(unittest.TestCase):
 
    def test_def_presense(self):
        test = create_presence_message('Guest')
        test[os.getenv('TIME')] = 1.1
        self.assertEqual(test, {os.getenv('ACTION'): os.getenv('PRESENCE'), 
                                os.getenv('TIME'): 1.1, 
                                os.getenv('USER'): {os.getenv('ACCOUNT_NAME'): 'Guest'}})

    def test_200_ans(self):
        self.assertEqual(parse_response({os.getenv('RESPONSE'): 200}), '200 : OK')

    def test_400_ans(self):
        self.assertEqual(parse_response({os.getenv('RESPONSE'): 400, os.getenv("ERROR"): 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        self.assertRaises(ValueError, parse_response, {os.getenv("ERROR"): 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
