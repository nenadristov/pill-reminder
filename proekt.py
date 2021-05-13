from datetime import datetime
import time

def pill_taken():
    #wave hand for taken
    
    if taken == True: return True
    else: return False

def timer(interval):
    stop = 0
    for i in range(interval):
        if pill_taken():
            print("Pij apce {}".format(pill_name[time_for_pill.index(i)]))
            api.fableSpeak(str('Take the {}'), "en".format(pill_name[time_for_pill.index(i)]))
        stop+=1
        time.sleep(1)
    
    if stop == interval-1 and pill_taken() == False:
        account_sid = 'AC07804832895d05568ef8134b1d51a263'
        auth_token = 'd95b620a88bd001126e27dc06eabc411'
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body="The person is 5min on his pill",
                            from_='+16789819653',
                            to='+38978980433'
                        )


time_for_pill = ["14:26"]
pill_name = ["red"]
interval_pills = 60

while True:
    print("waiting..")
    now = datetime.now()
    for i in time_for_pill:
        if now.strftime("%H:%M") == i:
            timer(300)
            #speak
        
    
    
