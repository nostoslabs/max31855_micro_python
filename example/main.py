from max31855 import MAX31855
from machine import SPI, Pin
from time import sleep

spi = SPI(1, baudrate=10_000_000, polarity=0, phase=0, sck=Pin(10), mosi=Pin(11), miso=Pin(8))
print(f"We got the following SPI values: {spi}")
cs = Pin(13, Pin.OUT)
print(f"We got the following CS values: {cs}")
tc = MAX31855(spi, cs)
while True:
    temp = tc.temp
    raw = tc.raw
    tempNIST = tc.temp_NIST
    tempC = tc.temp_c_fast
    tempF = tc.temp_f_fast

    print("Temperature: ", temp)
    print("Raw:", raw)
    print("Temperature NIST: ", tempNIST)
    print("Temperature C: ", tempC)
    print("Temperature F: ", tempF)
    print(" ")
    sleep(1)
