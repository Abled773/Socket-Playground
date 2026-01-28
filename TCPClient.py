
from socket import *
import sys



def main():

    #Error checking to handle commands that are faulty. Allowing for less faulty traffic.
    if(len(sys.argv) != 5): #check number of arguments
        print(f"Conversion command must take 5 arguments. User provided {len(sys.argv)}")
        sys.exit(1)
    
    #Check if the third argument is a float
    try:
        command = float(sys.argv[2])
    except ValueError:
        print (f"{sys.argv[2]} is not a valid float!")
        sys.exit(1)
    
    serverName = sys.argv[1]
    serverPort = 13333
    clientSocket = socket(AF_INET, SOCK_STREAM) #Create TCP socket
    
    try:# Check if the server name is valid
        clientSocket.connect((serverName,serverPort))
    except gaierror:
        print(f"Invalid server name: {serverName}")
        sys.exit(1)
    except ConnectionRefusedError:
        print(f"Connection refused")
        clientSocket.close()    
        sys.exit(1)

    #Send the command to the server, example: 100 km mi
    clientSocket.send(" ".join([sys.argv[2], sys.argv[3], sys.argv[4]]).encode()) 
    
    #Server Response
    conversion = clientSocket.recv(1024)
    print (f"From Server: {conversion.decode()}")
    clientSocket.close()

if __name__ == "__main__":
    main()