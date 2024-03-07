# MAX31855 MicroPython Library

This library provides an interface to interact with the MAX31855 thermocouple-to-digital converter using MicroPython. It allows for easy integration of temperature measurements into your MicroPython-based projects.

## Features

- Simple and intuitive API for temperature reading
- Support for both hardware and software SPI interfaces
- Error detection and reporting for common thermocouple faults

## Prerequisites

Before using this library, ensure that your hardware is compatible with MicroPython and that the firmware is properly flashed on your device.

## Installation

To install the MAX31855 MicroPython library, copy the library file to your MicroPython board's filesystem. This can typically be done using a file transfer tool appropriate for your board.

## Usage

After installation, import the library and initialize the MAX31855 object with the appropriate SPI and CS (chip select) pins:

```python
from max31855 import MAX31855
from machine import SPI, Pin

spi = SPI(1)
cs = Pin('X5', Pin.OUT)
max31855 = MAX31855(spi, cs)

temperature = max31855.read_temperature()
print("Temperature:", temperature, "°C")
```

Replace `'X5'` with the pin used for chip select on your board.

## Data Sheet

For more detailed information about the MAX31855, consult the [data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/max31855.pdf).

## Troubleshooting

If you encounter issues while using this library, double-check your wiring and ensure that your SPI settings (such as the clock speed and polarity) are correct for the MAX31855.

## Contributing

Contributions to this library are welcome. Please submit pull requests on GitHub or report any issues you encounter.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For additional support, consider consulting the MicroPython forums or the repository's issue tracker.
