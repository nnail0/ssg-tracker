"""
serves as the primary entry point 
for managing data. 
- uses info about the connection (handed from the ConnectionHandler)
  to grab data from serial and packaged in some sort of protocol 
  (either for our custom use case or NMEA). 
- responsible for making API calls on behalf of other modules and
  handing over the information, ideally in a format that is 
  easy for other modules to use off-the-bat. 
"""