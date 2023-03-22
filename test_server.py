import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from server import parse_message

class TestServer(unittest.TestCase):

    err_dict = {
        os.getenv('RESPONSE'): 400,
        os.getenv("ERROR"): 'Bad Request'
    }
    ok_dict = {os.getenv('RESPONSE'): 200}

    def test_no_action(self):
        """Ошибка если нет действия"""
        self.assertEqual(parse_message(
            {os.getenv('TIME'): '1.1', os.getenv('USER'): {os.getenv('ACCOUNT_NAME'): 'Guest'}}), self.err_dict)

    def test_wrong_action(self):
        """Ошибка если неизвестное действие"""
        self.assertEqual(parse_message(
            {os.getenv('ACTION'): 'Wrong', os.getenv('TIME'): '1.1', os.getenv('USER'): {os.getenv('ACCOUNT_NAME'): 'Guest'}}), self.err_dict)

    def test_no_time(self):
        """Ошибка, если  запрос не содержит штампа времени"""
        self.assertEqual(parse_message(
            {os.getenv('ACTION'): os.getenv('PRESENCE'), os.getenv('USER'): {os.getenv('ACCOUNT_NAME'): 'Guest'}}), self.err_dict)

    def test_no_user(self):
        """Ошибка - нет пользователя"""
        self.assertEqual(parse_message(
            {os.getenv('ACTION'): os.getenv('PRESENCE'), os.getenv('TIME'): '1.1'}), self.err_dict)

    def test_unknown_user(self):
        """Ошибка - не Guest"""
        self.assertEqual(parse_message(
            {os.getenv('ACTION'): os.getenv('PRESENCE'), os.getenv('TIME'): 1.1, os.getenv('USER'): {os.getenv('ACCOUNT_NAME'): 'Guest1'}}), self.err_dict)

    def test_ok_check(self):
        """Корректный запрос"""
        self.assertEqual(parse_message(
            {os.getenv('ACTION'): os.getenv('PRESENCE'), os.getenv('TIME'): 1.1, os.getenv('USER'): {os.getenv('ACCOUNT_NAME'): 'Guest'}}), self.ok_dict)


if __name__ == '__main__':
    unittest.main()
