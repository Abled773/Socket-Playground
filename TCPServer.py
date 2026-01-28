from socket import *



def main():

    #Initialize server
    serverPort = 13333
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)

    print("The server is ready to receive")

    #Server loop
    while True:

        #Accept connection from client
        connectionSocket, addr = serverSocket.accept()
        print("Connection from:", addr)

        #decode command from client
        command = connectionSocket.recv(1024).decode()
        command = command.lower().split()
        
        #Check data again in case there is a command that did not run through the proper client

        # Check number of arguments
        if len(command) != 3:
            connectionSocket.send(f"Invalid number of arguments: There must be 3, client sent {len(command)}")
            continue
        
        # Check if the first argument is a float
        try:
            command[0] = float(command[0])
        except ValueError:
            connectionSocket.send(f"{command[0]} is not a valid float!".encode())
            continue
        


        message = ""


        if command[1] == 'mi' or command[1] == 'km':
            message = length(command[0], command[1], command[2])
        elif command[1] == 'lb' or command[1] == 'kg':
            message = weight(command[0], command[1], command[2])
        elif command[1] == 'c' or command[1] == 'f':
            message = temp(command[0], command[1], command[2])
        else:
            message = f" {command[1]} is not a valid unit."
        connectionSocket.send(message.encode())
        
                







def length(distance: float, initial_unit: str, conversion: str):
    

    if (initial_unit == 'km' and conversion == 'mi'):
        converted = distance * 0.621371
        return f"{distance: .3f} kilometers is{converted: .3f} miles."

    elif(initial_unit == 'mi' and conversion == 'km'):
        converted = distance / 0.621371
        return (f"{distance: .3f} miles is{converted: .3f} kilometers.")
            
    
    else:
        return f"{conversion} is not a valid unit paired with {initial_unit}."




def weight(weight: float, initial_unit: str, conversion: str):
    
    if (initial_unit == 'lb' and conversion == 'kg'):
        converted = weight * 0.4535924
        return f"{weight: .3f} pounds is{converted: .3f} kilograms."
        

    elif(initial_unit == 'kg' and conversion == 'lb'):
        converted = weight / 0.4535924
        return (f"{weight: .3f} kilograms is{converted: .3f} pounds.")
           
    
    else:
        return f"{conversion} is not a valid unit paired with {initial_unit}."





def temp(temp: float, initial_unit: str, conversion: str):
    
    #Celsius to Farenheit
    if (initial_unit == 'c' and conversion == 'f'):
        converted = (temp * 1.8) + 32
        return (f"{temp: .3f} celsius is{converted: .3f} farenheit.")
        
    #Farenheit to Celsius
    elif(initial_unit == 'f' and conversion == 'c'):
        converted = (temp - 32)/1.8
        return (f"{temp: .3f} farenheit{converted: .3f} celsius.")
            
    # Invalid conversion unit
    else:
        return f"{conversion} is not a valid unit paired with {initial_unit}."

 


if __name__ == "__main__":
    main()