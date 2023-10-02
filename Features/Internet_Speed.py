def Int_Speed():  
    from Body.Speak import Speak  
    import speedtest
    wifi  = speedtest.Speedtest()
    raw_upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
    raw_download_net = wifi.download()/1048576
    upload_net = round(raw_upload_net , 2)
    download_net = round(raw_download_net , 2)
    Speak(f"Wifi download speed is {download_net} Mbps")
    Speak(f"Wifi Upload speed is {upload_net} Mbps") 

