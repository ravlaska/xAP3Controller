# xAP3Controller
<b>A Docker container that automates Xiaomi Air Purifier 3C operation.</b>
<br><br>
Requirements:
`docker, docker-compose`
<br>
In case using it on Raspberry Pi Raspbian need to be 64-bit version.
<br><br>
<b>
Usage:
</b>
Download script:

`git clone https://github.com/ravlaska/xAP3Controller.git`

`cd xAP3Controller`

Put IP and TOKEN values between apostrophes in main.py file (you can edit rest of user's variables, but you don't have to):

`nano main.py`


Build and start container:

`chmod +x run.sh`

`./run.sh`
