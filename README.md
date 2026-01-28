Gavin Robertson
gcr592s@login.missouristate.edu
CSC 625
Socket Programming Assignment
10/8/25

# Available Conversions Pairs
Each pair can convert to each other. If you attempt to convert metrics not of the same type, you will get an error.

miles <--> kilometers
pounds <--> kilograms
farenheit <--> celsius

the accepted forms of the metrics is shortened to be

mi, kg, lb, kg, f, c

UNITS ARE NOT CASE SENSITIVE


# Description of each file

## TCP

### TCPServer.py
Runs on port 13333

Running this file initializes a TCP server that accepts the command in the form

<measurement> <from_metric> <to_metric>

If the command is suitable for conversion, then it will send the string to the client that states the conversion.

If the command is not suitable, then it will tell the client


### TCPClient.py
Connects on port 13333

File must be ran with 4 user-defined arguments. Totaling to 5 arguments including python3

These arguments are:

<TCPClient.py> <hostname/IP> <measurement> <from_metric> <to_metric>

If the command is suitable for conversion then the <measurement> <from_metric> <to_metric> will send to the server.

Once the conversion is complete, recieves the conversion string 

## UDP

### UDPServer.py
Runs on port 13334
Running this file initializes a UCP server that accepts the command in the form

<measurement> <from_metric> <to_metric>

If the command is suitable for conversion, then it will send the string to the client that states the conversion.

If the command is not suitable, then it will tell the client.


### UDPClient.py
Connects on port 13334

File must be ran with 4 user-defined arguments. Totaling to 5 arguments

These arguments are:

TCPClient.py <hostname/IP> <measurement> <from_metric> <to_metric>

If the command is suitable for conversion then the <measurement> <from_metric> <to_metric> will send to the server.

Once the conversion is complete, recieves the conversion string 

If the UDPSever times out, or connection is refused. The client will try to send the data two more times.



# Compilation/Execution Instructions
Check if ports are available

On TCP: run
netstat -an | find "13333"

On UDP: run
netstat -an | find "13334"

For both UDP and TCP you must initialize the server using

python3 TCPServer.py
or
Python3 UDPServer.py

Then you will see confirmation that the server is ready in the servers terminal

Then run the the corresponding client file
The both client files takes 5 arguments, with 4 of the arguments being defined
in the form:

python3 UDPClient.py <hostname> <measurement> <from_metric> <to_metric>
python3 TCPClient.py <hostname> <measurement> <from_metric> <to_metric>
if you are running both files on your machine then the hostname is most likely localhost

for e.g

python3 UDPClient.py localhost 100 mi kg

python3 TCPclient.py localhost 100 f c

# Detailed Protocol Guide

TCP: 13333
UDP: 13334

Command
<measurement> <from_unit> <to_unit>
Example: 100 mi km

View 
# Available Conversions Pairs
for what is possible to convert

- Success: <measurement> <from_unit> = <converted_value> <to_unit>
  Example: From Server: 100.000 celsius is 212.000 farenheit.
- Error: <error message>
  Example: km is not a valid unit paired with kg.

UDP Error-Checking: client retries up to 3 times with 2-second timeout if no response.
Error conditions: malformed request, unsupported unit, incompatible units

# Limitations
Does not check all possible network errors.
Does not have a variety of conversions to choose from

