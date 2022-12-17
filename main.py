import os
from miio import AirPurifierMiot
from miio.integrations.airpurifier.zhimi.airpurifier_miot import OperationMode
from datetime import datetime

# Loading user's variables
############################################################################
IP = ''										# IP of AP3C
TOKEN = ''									# TOKEN of AP3C

refresh = str(30)							# refresh rate in seconds

swk = [4, 7]								# on/off switch [value to turn off, value to turn on]
led_DN = [4, 1]								# led brightness level (0-8) [day value, night value]
hour_DN = [6, 23]							# start hour of [day, night]

# RPM tables values:

limits = [10, 15, 25, 30, 45, 50]			# values for modes in RPM tables (4 modes limits: <10, 15 < 25, 30 < 45, >50)

											# working modes for RPM tables (values between 0 - 2000)
lowL = 400
lowH = 800
mediumL = 1000
mediumH = 1510
highL = 1800
highH = 1950
############################################################################

# Connecting with AP3C
ap = AirPurifierMiot(IP, TOKEN)

# Turning on favorite mode
ap.set_mode(OperationMode.Favorite)

# Main loop
while True:

	# Defining data from device
	now = int(datetime.now().strftime("%H"))  # current time
	aq = ap.status().aqi  # current pm2.5
	io = ap.status().power  # current power status
	mode = str(ap.status().mode)  # current working mode
	led = ap.status().led_brightness_level  # current led level


	# Checking AP3C working mode
	if mode == 'OperationMode.Favorite':

		# Turning off
		if (aq < swk[0]) & (io == 'on'):
			ap.off()
			io = ap.status().power

		# Turning on
		if (aq > swk[1]) & (io == 'off'):
			ap.on()
			io = ap.status().power

		# Check if AP3C is off
		if io == 'on':

			# Day rules
			if (now < hour_DN[1]) & (now > hour_DN[0]):

				# Brightening led
				if (led == led_DN[1]):
					ap.set_led_brightness_level(led_DN[0])		

				# Table of RPMs
				if aq < limits[0]:  					 # 10
					ap.set_favorite_rpm(lowL)
				if (aq > limits[1]) & (aq < limits[2]):  # 15 < 25
					ap.set_favorite_rpm(mediumH)
				if (aq > limits[3]) & (aq < limits[4]):  # 30 < 45
					ap.set_favorite_rpm(highL)
				if aq > limits[5]: 						 # 50
					ap.set_favorite_rpm(highH)

			# Night rules
			else:

				# Dimming led
				if led == led_DN[0]:
					ap.set_led_brightness_level(led_DN[1])

				# Table of RPMs
				if aq < limits[0]:  					 # 10
					ap.set_favorite_rpm(lowL)
				if (aq > limits[1]) & (aq < limits[2]):  # 15 < 25
					ap.set_favorite_rpm(lowH)
				if (aq > limits[3]) & (aq < limits[4]):  # 30 < 45
					ap.set_favorite_rpm(mediumL)
				if aq > limits[5]:  					 # 50
					ap.set_favorite_rpm(mediumH)
			
	# Refreshing rate
	os.system('sleep ' + refresh)
