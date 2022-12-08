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

    

    print("Enter the info you want to send")
    name = "hello"
    account = "A345789"


    atClient.put_public('attalk', name)
    atClient.put_public('account', account)
    print(name, " and", account, " have been sent to the server")

         
            
                

##########################################################
        
    


  


if __name__ == "__main__":
    main()