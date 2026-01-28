from socket import *
import sys

def main():
    #Initialize UDP server
    serverPort = 13334
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print("The server is ready to receive")
    
    #Sever loop
    while True:
        command, addr = serverSocket.recvfrom(2048)
        command = command.decode().lower().split()
        
        #Check data again in case there is a command that did not run through the proper client
        
        if len(command) != 3:
            serverSocket.sendto(f"Invalid number of arguments: There must be 3, client sent {len(command)}", addr)
            continue
        
        #Check if the first argument is a float
        try:
            command[0] = float(command[0])
        except ValueError:
            serverSocket.sendto(f" {command[0]} is not a valid float!".encode(), addr)
            continue
        

        
        
        message = ""
        
        #Conversion logic
        if command[1] == 'mi' or command[1] == 'km':
            message = length(float(command[0]), command[1], command[2])
        elif command[1] == 'lb' or command[1] == 'kg':
            message = weight(float(command[0]), command[1], command[2])
        elif command[1] == 'c' or command[1] == 'f':
            message = temp(float(command[0]), command[1], command[2])
        else:
            message = f" {command[1]} is not a valid unit."
        
        serverSocket.sendto(message.encode(), addr)



def length(distance: float, initial_unit: str, conversion: str):
    

    if (initial_unit == 'km' and conversion == 'mi'):
        converted = distance * 0.621371
        return f"{distance: .3f} kilometers is{converted: .3f} miles."

    elif(initial_unit == 'mi' and conversion == 'km'):
        converted = distance / 0.621371
        return f"{distance: .3f} miles is{converted: .3f} kilometers."
            
    
    else:
        return f"{conversion} is not a valid unit paired with {initial_unit}."


def weight(weight: float, initial_unit: str, conversion: str):
    if (initial_unit == 'lb' and conversion == 'kg'):
        converted = weight * 0.4535924
        return (f"{weight: .3f} pounds is{converted: .3f} kilograms.")
        

    elif(initial_unit == 'kg' and conversion == 'lb'):
        converted = weight / 0.4535924
        return (f"{weight: .3f} kilograms is{converted: .3f} pounds.")
           
    
    else:
        return f"{conversion} is not a valid unit paired with {initial_unit}."


def temp(temp: float, initial_unit: str, conversion: str):
    if (initial_unit == 'c' and conversion == 'f'):
        converted = (temp * 1.8) + 32
        return (f"{temp: .3f} celsius is{converted: .3f} farenheit.")
        

    elif(initial_unit == 'f' and conversion == 'c'):
        converted = (temp - 32)/1.8
        return (f"{temp: .3f} farenheit{converted: .3f} celsius.")
            
    
    else:
        return f"{conversion} is not a valid unit paired with {initial_unit}."



if __name__ == "__main__":
    main()