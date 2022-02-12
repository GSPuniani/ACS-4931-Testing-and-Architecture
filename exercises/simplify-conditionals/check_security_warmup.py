def send_alert():
   print("alert!")

def check_security(people):
   for p in people:
        if p == "Naruto" or p == "Goku":
            send_alert()
            break
          
      
check_security(["Kami", "Naruto"])
