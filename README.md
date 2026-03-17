# Discord Auto Messenger

A simple Python script that automatically sends messages to a Discord channel.

Setup on Termux (Step-by-Step)
1️⃣ Update Termux
Copy code
Bash
pkg update
pkg upgrade
2️⃣ Install Python
Copy code
Bash
pkg install python
Check version:
Copy code
Bash
python --version
3️⃣ Install discord library
Copy code
Bash
pip install discord.py
4️⃣ Create the file
Copy code
Bash
nano dc.py
Paste your script.
Save:
Copy code

CTRL + X
Y
ENTER
5️⃣ Run the script
Copy code
Bash
python dc.py
If the token works you will see:
Copy code

Logged in as YourName
5. Running 24/7 on Termux
If you want it running while the screen is off:
Install wakelock:
Copy code
Bash
termux-wake-lock
Then run:
Copy code
Bash
python dc.py
How to run it?
Changes in Nano Dc.py
Replace channel id , token , message
And Python Dc.py 
To run
Thanks...
