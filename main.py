import requests, random, time

def generate_random_message():
    text = [
        "Hollo",

    ]
    rand_mess = random.choice(text)
    return rand_mess

def create_data(message):
    return {'content': message}

def create_headers():
    randtoken = ['TOKEN1',"TOKIN2"]
    token = random.choice(randtoken)
    return {'authorization': token}

def send_response():
    sent_messages = 0
    while True:
        rand_mes = generate_random_message()
        header = create_headers()
        payload = create_data(rand_mes)

        try:
            r = requests.post('https://discord.com/api/v9/channels/1193166796220542996/messages', data=payload, headers=header)
            if r.status_code == 200:
                sent_messages += 1
                print(f"[{sent_messages}]Message sent: {rand_mes}")
            elif r.status_code == 403:
                print(f"The Token Is Invalid")
            else:
                print(f"Failed to send message. Status code: {r.status_code}")
        except requests.RequestException as e:
            print(f"Request Exception: {e}")

        time.sleep(3)

send_response()