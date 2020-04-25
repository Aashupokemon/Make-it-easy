import os
os.system("tput setaf 1")
print("\t\t\t WELCOME TO TUI")
os.system("tput setaf 7")
print("\t\t\t --------------")
passwd = input("Enter your password: ")
apass="ayush"
if passwd != apass:
    print("Incorrect password")
    exit()
print("choose local/remote",end=" : ")
location=input()
print(location)
os.system("clear")
if location=="remote":
    remoteIP=input("Enter the IP Address")
while True:
    os.system("tput setaf 15")
    print("""
    Press 1: To see the date           Press 8: To launch ubuntu
    Press 2: To see the calendar       Press 9: To create Docker Image
    Press 3: To configure Web Server   Press 10: To launch mysql server            
    Press 4: To create File            Press 11: To start docker
    Press 5: To create Directory       Press 12: To stop docker
    Press 6: To create User            Press 13: To pull a docker image
    Press 7: To launch pyhton console  Press 14: To exit the TUI
    """)


    print("Enter your choice",end=" : ")
    ch=input()
    if location=="local":
        if int (ch)==1:
            os.system("date")
        elif int (ch)==2:
            os.system("cal")
        elif int (ch)==3:
            os.system("yum install httpd")
            os.system("systemctl start httpd")
            os.system("systemctl enable httpd")
            os.system("systemctl status httpd")
        elif int (ch)==4:
            print("Enter file name please",end=" : ")
            File_name=input()
            os.system("touch {0}".format(File_name))
        elif int (ch)==5:
       elif int (ch)==5:
            print("Enter directory name please",end=" : ")
            Dir_name=input()
            os.system("mkdir {0}".format(Dir_name))
        elif int (ch)==6:
            print("Enter the username please",end=" : ")
            User_name=input()
            os.system("useradd {0}".format(User_name))
        elif int (ch)==7:
            os.system("python3")
        elif int (ch)==8:
            os.system("systemctl start docker")
            os.system("docker run -it --name MYOS ubuntu:14.04")
        elif int (ch)==9:
            Img_name=input("Enter image name : " )
            os.system("docker commit {0}".format(Img_name))
        elif int (ch)==10:
            os.system("systemctl restart docker")
            os.system("docker run -it -e MYSQL_ROOT_PASSWORD=redhat mysql:5.7")
        elif int (ch)==11:
            os.system("systemctl start docker")
        elif int (ch)==12:
            os.system("systemctl stop docker")

elif int (ch)==13:
            Doc_img=input("Enter image to pull : ")
            os.system("docker pull {0}".format(Doc_img))
        elif int (ch)==14:
            print("\t\t\texiting....")
            exit()
        else:
            print("TRY AGAIN!")

        input("Enter to continue... ")
        os.system("clear")

    elif location=="remote":
        if int (ch)==1:
            os.system("ssh {0} date".format(remoteIP))
        elif int (ch)==2:
            os.system("ssh {0} cal".format(remoteIP))
        elif int (ch)==3:
            os.system("ssh {0} yum install httpd".format(remoteIP))
            os.system("ssh {0} systemctl start httpd".format(remoteIP))
            os.system("ssh {0} systemctl enable httpd".format(remoteIP))
            os.system("ssh {0} systemctl status httpd".format(remoteIP))
        elif int (ch)==4:

            print("Enter file name please",end=" : ")
            File_name=input()
            os.system("ssh {0} touch {1}".format(remoteIP,File_name))
        elif int (ch)==5:
            print("Enter directory name please",end=" : ")
            Dir_name=input()
            os.system("ssh {0} mkdir {1}".format(remoteIP,Dir_name))
        elif int (ch)==6:
            print("Enter the username please",end=" : ")
            User_name=input()
            os.system("ssh {0} useradd {1}".format(remoteIP,User_name))
        elif int (ch)==7:
            os.system("ssh {0} python3 {1}".format(remoteIP))
        elif int (ch)==8:
            os.system("ssh {0} systemctl start docker {1}".format(remoteIP))
            os.system("ssh {0} docker run -it --name MYOS ubuntu:14.04".format(remoteIP))
        elif int (ch)==9:
            Img_name=input("Enter image name : " )
            os.system("ssh {0} docker commit {1}".format(remoteIP,Img_name))
        elif int (ch)==10:
            os.system("ssh {0} systemctl restart docker {1}".format(remoteIP))
            os.system("ssh {0} docker run -it -e MYSQL_ROOT_PASSWORD=redhat mysq                            l:5.7 {1}".format(remoteIP))
        elif int (ch)==11:
            os.system("ssh {0} systemctl start docker".format(remoteIP))
        elif int (ch)==12:
            os.system("ssh {0} systemctl stop docker".format(remoteIP))
        elif int (ch)==13:
            Doc_img=input("Enter image to pull : ")
            os.system("ssh {0} docker pull {1}".format(remoteIP,Doc_img))

        elif int (ch)==14:
            print("\t\t\texiting....")
            exit()
        else:
            print("TRY AGAIN!")

        input("Enter to continue...")
        os.system("clear")

    else:
        print("Location Not Found!")


