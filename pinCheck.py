def main():
    from machine import Pin
    import utime
  
############### atSign ######################
    # read settings.json
    from lib.at_client import io_util
    ssid, psw, atSign = io_util.read_settings()
    del io_util # make space in memory

    # connect to wifi
    from lib import wifi
    print('Connecting to WiFi %s...' % ssid)
    wifi.init_wlan(ssid, psw)
    del ssid, psw, wifi # make space in memory

    # connect and pkam authenticate into secondary
    from lib.at_client import at_client
    atClient = at_client.AtClient(atSign, writeKeys=True)
    atClient.pkam_authenticate(verbose=True)
    del at_client
##############################################

    # Create a map between keypad buttons and characters
    matrix_keys = [['1', '2', '3', 'A'],
                ['4', '5', '6', 'B'],
                ['7', '8', '9', 'C'],
                ['*', '0', '#', 'D']]

    # Define PINs according to cabling
    keypad_rows = [9,8,7,6]
    keypad_columns = [5,4,3,2]


    col_pins = []
    row_pins = []

    ## the keys entered by the user
    guess = []
   
    secret_pin = ['1','2','3','4','5','6']
    #setup pin to be an output
    led = Pin("LED", Pin.OUT)

    for x in range(0,4):
        row_pins.append(Pin(keypad_rows[x], Pin.OUT))
        row_pins[x].value(1)
        col_pins.append(Pin(keypad_columns[x], Pin.IN, Pin.PULL_DOWN))
        col_pins[x].value(0)



    
##############################Scan keys ####################
    
    def scankeys():
        
        for row in range(4):
            for col in range(4): 
                row_pins[row].high()
                key = None
                
                if col_pins[col].value() == 1:
                    print("You have pressed:", matrix_keys[row][col])
                    key_press = matrix_keys[row][col]
                    utime.sleep(0.3)
                    guess.append(key_press)
                
                    
                if len(guess) == 6:
                    checkPin(guess)
                    
                    for x in range(0,6):
                        guess.pop() 
                        
            row_pins[row].low()
        

    ############################## To check Pin #################
    def checkPin(guess):
                
        if guess == secret_pin:
            atClient.put_public('led', "".join(map(str,guess)))
            print("You got the pin correct")
            led.value(1)
            utime.sleep(3)
            led.value(0)
            
        else:
            print("Pin incorrect, try agian")     
            
                

    ##########################################################
        
    print("Enter the secret Pin")


    while True:
        
        scankeys()


if __name__ == "__main__":
    main()