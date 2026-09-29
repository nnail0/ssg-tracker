"""
lora_connection.py
Handle connections for LoRa radio using necessary libraries. 

NOTE: some people from comms will be needed to get necessary pins. 
"""

import LoRaRF as LoRa;

def connect() -> int:
    # connect to the lora module
    lora = LoRa.SX127x()
    lora.setFrequency(915000000)
    lora.setRxGain(lora.RX_GAIN_POWER_SAVING)
    if lora.begin() != 1:
        print("Issue starting communication. Please try again.")
    print("LoRa connection started with no issues.")



        
