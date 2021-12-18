import spidev
import time
import RPi.GPIO as GPIO

# create SPI object and start SPI connection
spi = spidev.SpiDev()
spi.open(0,0)

# Read MCP3008 data
def analogInput(adc_pin):
	spi.max_speed_hz = 1350000
	adc = spi.xfer2([1, (8 + adc_pin)<< 4, 0])
	data = ((adc[1] & 3) << 8) + adc[2]
	return data

while True:
	#Reading from CH0
	Output = analogInput(0)
	Output = interp(output, [0, 1023], [100, 0])
	Output = int(Output)
	print("------------------------------")
	print("Soil Moisture is  : ", Output)
	time.sleep(0.001)