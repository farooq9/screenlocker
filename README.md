# screenlocker
A screen locker ransomware is a type of malicious software (malware) that infects a computer system and restricts the user's access to their device by locking the screen. Once the ransomware is activated, it typically displays a full-screen message or image that informs the user that their computer has been locked.

The message displayed by the ransomware typically includes instructions on how to pay a ransom to the attacker in order to regain access to the computer. The ransom is usually demanded in a cryptocurrency such as Bitcoin, which makes it difficult to trace the payment back to the attacker and get the key.

<img width="754" alt="screenlocker" src="https://github.com/farooq9/screenlocker/assets/88651754/a42f0aff-1f0c-4ac9-9329-e6677e054546">

# About
The above displayed image is a demo of how the ransomeware looks after executing,
the message displayed can be altered accordingly.
It will lock all the keys on keyboard, the pin can entered by clicking the buttons with mouse.

# Usage
To Convert the .py file to .exe run the below command in PowerShell
pyinstaller -F -w screenlocker.py
You will find your new screenlocker.exe in dist folder.
Before creating exe file change your password from 12345

# requirements
keyboard & pyinstaller
pip install -r requirements.txt

# Warning
Never use this for Fun activities
This is created only for education purpose to gain knowledge on how the malware work. 
