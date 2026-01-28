from socket import *
import sys

def main():

    #Check for proper number of arguments
    if(len(sys.argv) != 5):
        print(f"Conversion command must take 5 arguments. User provided {len(sys.argv)}")
        sys.exit(1)
    
    #Check if the third argument is a float
    try:
        command = float(sys.argv[2])
    except ValueError:
        print(f"{sys.argv[2]} is not a valid float!")
        sys.exit(1)
    
    #Initialize UDP socket
    serverName = sys.argv[1]
    serverPort = 13334
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    clientSocket.settimeout(2)

    #Check if the server name is valid
    clientSocket.connect((serverName,serverPort))


    message = " ".join([sys.argv[2], sys.argv[3], sys.argv[4]])
    #Try to send the message 3 times before quitting
    for i in range(3):
        try:
            #Response from server
            clientSocket.sendto(message.encode(),(serverName, serverPort))
            conversion, serverAddress = clientSocket.recvfrom(2048)
            print(f"From Server:{conversion.decode()}")
            clientSocket.close()
            sys.exit(0)

        except ConnectionRefusedError:
            print(f"Connection refused, retry {i + 1}")
        except timeout:
            print(f"Timeout, retry {i + 1}")
    
    print("No response from server, exiting")
    clientSocket.close()    
    sys.exit(1)


if __name__ == "__main__":
    main()
