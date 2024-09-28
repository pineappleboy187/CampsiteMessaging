#Used for the Traccer sms gateway app.
import requests

# config area
import config

def send(number, message):
    try:
        x = requests.post(config.url, json={'to': number, 'message': message}, headers={"Authorization": config.api})
        if x.status_code == 200:
            return True
        else:
            return False

    except Exception as error:
        print("An exception occurred:", error)
        return False


def main():
    if send("+15873359944", "Hello"):
        print("Message sent")


main()

