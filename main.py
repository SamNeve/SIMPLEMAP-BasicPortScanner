import pyfiglet
import socket

def portScanner():
    print ("-" * 60)
    ascii_banner = pyfiglet.figlet_format("SIMPLEMAP")
    print(ascii_banner)
    print ("#Note this simple scanner is not multithreaded meaning\n#it can only scan one port at a time.")
    print ("#I would recommend only scanning a small range of ports!!!")
    print ("-" * 60)

    target = input("What is the targets IPv4 Address: ")
    firstPort = int(input("What is the first port you want to scan: "))
    secondPort = int(input("What is the last port you want to scan: "))

    for port in range(firstPort,secondPort + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target, port))

        if result == 0:
            print ("Port " + str(port) + " is open")
        else:
            print ("Port " + str(port) + " is closed")

        #If you dont want to see the closed ports
        #except:
            #pass

        sock.close()

portScanner()







