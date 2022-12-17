# xAP3Controller
<b>A Docker container that automates Xiaomi Air Purifier 3C operation.</b>
<br><br><b>
Requirements:</b>
`docker, docker-compose`
<br>
In case using it on Raspberry Pi Raspbian need to be 64-bit version.
<br><br>
<b>
Usage:
<br><br>
Download script:
</b><br>
`git clone https://github.com/ravlaska/xAP3Controller.git`
<br>
`cd xAP3Controller`
<b><br><br>
Put IP and TOKEN values between apostrophes in main.py file (you can edit rest of user's variables, but you don't have to):
  </b><br>
`nano main.py`

<b>
Build and start the container:</b>

`chmod +x run.sh`<br>
`./run.sh`
