import unittest
import physical_units_utils


class Test_PhysicalUnitsUtils(unittest.TestCase):
    """
    Class for testing  functions in physical_units_utils
    """ 
    def test_convert_speed(self):
        """
        Test case for the convert_speed function.
        Tests:
        - conversion of the same units
        - conversion from mph to kph
        - conversion from kph to mph
        - raising ValueError for invalid unit type
        - raising ValueError for invalid value type
        """
        # Test for same units
        result = physical_units_utils.convert_speed(75, 'kph', 'kph')
        self.assertEqual(result, 75)
        # Test for same units
        result = physical_units_utils.convert_speed(75, 'mph', 'mph')
        self.assertEqual(result, 75)
        # Test for mph to kph conversion
        result = physical_units_utils.convert_speed(50, 'mph', 'kph')
        self.assertAlmostEqual(result, 80.4672, places=4)
        # Test for kph to mph conversion
        result = physical_units_utils.convert_speed(100, 'kph', 'mph')
        self.assertAlmostEqual(result, 62.1371, places=4)

        # Test case for invalid unit type
        with self.assertRaises(ValueError):
            physical_units_utils.convert_speed(50, 'kmph', 'mph')

        # Test case for invalid value type
        with self.assertRaises(ValueError):
            physical_units_utils.convert_speed('yes', 'kph', 'mph')

    def test_convert_temperature(self):
        """
        Test case for the convert_temperature function.
        Tests:
        - conversion of the same units
        - conversion from Celsius to Fahrenheit
        - conversion from Fahrenheit to Celsius
        - raising ValueError for invalid unit type
        - raising ValueError for invalid value type
        """
        # Test for same units
        result = physical_units_utils.convert_temperature(75, 'C', 'C')
        self.assertEqual(result, 75)
        # Test for same units
        result = physical_units_utils.convert_temperature(75, 'F', 'F')
        self.assertEqual(result, 75)
        # Test for C to F conversion
        result = physical_units_utils.convert_temperature(50, 'C', 'F')
        self.assertAlmostEqual(result, 122, places=4)
        # Test for F to C conversion
        result = physical_units_utils.convert_temperature(100, 'F', 'C')
        self.assertAlmostEqual(result, 37.7778, places=4)

        # Test case for invalid unit type
        with self.assertRaises(ValueError):
            physical_units_utils.convert_temperature(50, 'Celsis', 'F')

        # Test case for invalid value type
        with self.assertRaises(ValueError):
            physical_units_utils.convert_temperature('yes', 'C', 'F')

    def test_convert_length(self):
        """
        Test case for the convert_lenght function.
        Tests:
        - conversion of the same units
        - conversion from m to feet
        - conversion from feet to m
        - raising ValueError for invalid unit type
        - raising ValueError for invalid value type
        """
        # Test case for same units
        result = physical_units_utils.convert_length(75, 'm', 'm')
        self.assertEqual(result, 75)
        # Test case for same units
        result = physical_units_utils.convert_length(75, 'ft', 'ft')
        self.assertEqual(result, 75)
        # Test case for m to ft conversion
        result = physical_units_utils.convert_length(50, 'm', 'ft')
        self.assertAlmostEqual(result, 164.042, places=4)
        # Test case for ft to m conversion
        result = physical_units_utils.convert_length(100, 'ft', 'm')
        self.assertAlmostEqual(result, 30.48, places=4)
        # Test case for invalid unit type

        with self.assertRaises(ValueError):
            physical_units_utils.convert_length(50, 'kilometer', 'm')

        # Test case for invalid value type
        with self.assertRaises(ValueError):
            physical_units_utils.convert_length('yes', 'm', 'ft')


if __name__ == '__main__':
    unittest.main()
