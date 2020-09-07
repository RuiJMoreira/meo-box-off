# meo-box-off
A python script to turn off the meo box.

You can use this script to turn off, or keep off, your meo box when you turn on your other set top box that runs python.
To achive this on your linux set top box you can use the crontab @reboot option - on other operating systems you can try other services to achive the same goal of runing the script at boot.

In alternative to turning off the meo box, you can also pause a stream by changing the line "s.sendall(b"key=151\n")" to "s.sendall(b"key=119\n")".
