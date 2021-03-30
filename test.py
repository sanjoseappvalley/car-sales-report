import json
import unittest
from unittest.mock import patch, MagicMock
from cars import load_data, format_car, process_data, cars_dict_to_table


class CarTest(unittest.TestCase):

    def test_load_json_data(self):
        p1 = patch("builtins.open", MagicMock())
        m = MagicMock(side_effect=[{"foo": "bar"}])
        p2 = patch("json.load", m)

        jsonfile = "car_sales.json"
        with p1 as p_open:
            with p2 as p_json_load:
                f = load_data(jsonfile)
        self.assertEqual({"foo": "bar"}, f)

    def test_format_car(self):
        car = {"car_make": "German", "car_model": "BMW", "car_year": 2022}
        carinfo = format_car(car)
        self.assertEqual(carinfo, "German BMW (2022)")

    def test_process_data_into_summary(self):
        data = [
            {"id": 1, "car": {"car_make": "F1", "car_model": "CW", "car_year": 1997}, "price": "$20.00", "total_sales": 2},
            {"id": 2, "car": {"car_make": "V1", "car_model": "Jet", "car_year": 2009}, "price": "$25.11", "total_sales": 5},
            {"id": 3, "car": {"car_make": "P1", "car_model": "RR", "car_year": 1997}, "price": "$12.30", "total_sales": 4}]

        summary = process_data(data)
        self.assertEqual(
            summary,
            ["The V1 Jet (2009) generated the most revenue: $125.55",
             "The Jet had the most sales: 5",
             "the most popular year was 1997 with 6 sales."]
        )

    def test_turn_car_data_to_table_data(self):
        data = [
            {"id": 1, "car": {"car_make": "F1", "car_model": "CW", "car_year": 1997}, "price": "$20.00", "total_sales": 2},
            {"id": 2, "car": {"car_make": "V1", "car_model": "Jet", "car_year": 2009}, "price": "$25.11", "total_sales": 5},
            {"id": 3, "car": {"car_make": "P1", "car_model": "RR", "car_year": 1997}, "price": "$12.30", "total_sales": 4}]

        table_data = cars_dict_to_table(data)
        self.assertEqual(
            table_data,
            [["ID", "Car", "Price", "Total Sales"],
             [1, "F1 CW (1997)", "$20.00", 2],
             [2, "V1 Jet (2009)", "$25.11", 5],
             [3, "P1 RR (1997)", "$12.30", 4]]
        )


if __name__ == "__main__":
    unittest.main()
