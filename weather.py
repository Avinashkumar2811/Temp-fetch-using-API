import requests

code=True
while True:
    BASE_URL= "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY= "c4ce13121d3b81fe7eae0377cac65b14" #my api
    CITY= input("ENTER YOUR CITY NAME:" ) #user input

    def tempchnage_k_to_c(kelvin): #function to change temp
        celsius=kelvin-273.15
        return celsius

    url=BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response=requests.get(url).json() #get kr rhe hain response ko
    #print(response)

    #for valid city
    if response["cod"]==200:
        temp_kelvin=response["main"]["temp"]
        temp_celsius=tempchnage_k_to_c(temp_kelvin)

        rounded_temp_celsius=round(temp_celsius,2) #round upto 2 decimal places

        print("The temperature in city:", CITY , "is" , rounded_temp_celsius, "°C")

    #for invalid city
    else:
        print("ERROR....INVALID CITY")



    #for repeatitive city check
    print("--------------------")
    choice=input("TYPE yes for another city temp, ELSE type no to stop: ")
    print("--------------------")
    
    if choice=="YES" or choice=="Yes" or choice=="yes":
        code=True
    
    else:
        print("THANKS FOR USING THIS WIDGET")
        break