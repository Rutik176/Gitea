import datetime
def say_good_night():
    current_time = datetime.datetime.now()
    current_hour = current_time.hour

    if current_hour <12:
        print ("say_good_night")
    else:
        print ("so jao")