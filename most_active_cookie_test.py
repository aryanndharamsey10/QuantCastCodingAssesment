import unittest
import most_active_cookie

class CookieMonsterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = most_active_cookie.CookieMonster()
        self.app.raw_data = [
            "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00",
            "5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00",
            "AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00",
            "SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00",
            "fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00",
            "4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00",
        ]
        self.app.parse_data()

    def test_parse_date_test(self):
        input_date = "2018-12-01T14:10:00+00:00"
        output_date = "2018-12-01"
        self.assertEqual(self.app.parse_date(input_date), output_date)

    def test_find_most_used_test_one(self):
        input_date = "2018-12-09"
        output_cookie = ["AtY0laUfhglK3lC7"]
        self.assertEqual(self.app.find_most_used(input_date), output_cookie)

    def test_find_most_used_test_two(self):
        input_date = "2018-12-08"
        output_cookie = ["SAZuXPGUrfbcn5UA",
                        "4sMM2LxV07bPJzwf",
                        "fbcn5UAVanZf6UtG"]
        self.assertEqual(self.app.find_most_used(input_date), output_cookie)


if __name__ == '__main__':
    unittest.main()