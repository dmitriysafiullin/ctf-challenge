import http.client
import json


def challenge_1():
    """Hint: I would like to get read I think"""
    try {
      File myObj = new File("filename.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        System.out.println(data);
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }

def challenge_2(data):
    """thiH: tnih a uoy evig lliw siht ebyaM"""
    data = read_data()
    return data


def challenge_3(data):
    """Hint: We are too low, we need to go higher up, just in case."""
    for data in data:
        return data


def send_it(name, number, email, api_key):
    """If you've got it then fill in your name and phone number then send it!"""
    host = "demo.lime-crm.com"
    endpoint = "/ctf_challenge/api/v1/limeobject/winner/"
    body = json.dumps({"name": name, "phone": number, "email": email})
    method = "POST"

    headers = {"x-api-key": api_key, "Content-Type": "application/json"}

    conn = http.client.HTTPSConnection(host)

    conn.request(method, endpoint, headers=headers, body=body)

    response = conn.getresponse()
    body = response.read()

    try:
        body = json.loads(body)
    except Exception:
        pass

    print("\nResponse:\n")
    print(f"Status code: {response.status}\n")
    print(f"Headers: {response.headers}")
    print(f"Body: {body}")

    if response.status and response.status > 199 and response.status < 300:
        print("\nCongratulations! Your name has been added to the list of winners")


if __name__ == "__main__":
    data_1 = challenge_1()

    data_2 = challenge_2(data_1)

    api_key = challenge_3(data_2)

    # If you think you've got it then send it. Just remember to fill in the credentials (optional)
    send_it(
        "YOUR_NAME_HERE",
        "12345678",
        "your_email@email.net",
        api_key,
    )
