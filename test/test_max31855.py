import unittest
from unittest.mock import MagicMock
from max31855 import MAX31855  # Import the MAX31855 class you want to test


# Mock for the machine.SPI class
class MockSPI:
    def __init__(self):
        self.readinto = MagicMock()


# Mock for the machine.Pin class
class MockPin:
    def __init__(self, pin):
        self.low = MagicMock()
        self.high = MagicMock()


class TestMAX31855(unittest.TestCase):
    def setUp(self):
        self.mock_spi = MockSPI()
        self.mock_cs = MockPin('CS pin')
        self.max31855 = MAX31855(self.mock_spi, self.mock_cs)

    def test_connection_error(self):
        # Mock data representing a thermocouple not connected error
        self.mock_spi.readinto.return_value = None
        self.max31855.data = bytearray([0x00, 0x00, 0x00, 0x01])
        with self.assertRaises(RuntimeError) as context:
            self.max31855.temp
        self.assertIn('thermocouple not connected', str(context.exception))

    def test_read_temp_c_fast(self):
        # Mock data representing a temperature reading
        self.mock_spi.readinto.return_value = None
        self.max31855.data = bytearray([0x00, 0x64, 0x00, 0x00])  # 100°C temperature data
        expected_temperature = 25.0  # As temp reading is shifted right by 2, 100 >> 2 = 25
        temperature = self.max31855.temp_c_fast
        self.assertEqual(temperature, expected_temperature)

    # Additional tests for the other methods and error conditions would follow...

if __name__ == '__main__':
    unittest.main()
