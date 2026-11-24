import requests

class StudentDao:

    #When a StudentDao object is created, several things happen.
    #The required headers are defined as a class member.
    #The base URL is defined as a class member.
    #An authentication token is generated and stored as a class member.
    #The token is valid for an hour before expiring.
    #The class members are available to all methods in the class.
    #They are used to make requests to the Oracle APEX API.

    def __init__(self):
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml",
            "accept-language": "en-GB,en-US",
            "sec-fetch-dest": "document",
            "user-agent": (
                "Mozilla/5.0 (iPad; CPU OS 18_5 like Mac OS X) "
                "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                "Version/18.5 Mobile/15E148 Safari/604.1"
            ),
        }

        self.base_url = "https://oracleapex.com/ords/is22082/"
        client_id = "7cyvcpfdn8tQkrezKYQLEA.."
        client_secret = "6jBgOg2iHHaPJQg3rvPgsg.."

        response = requests.post(
            self.base_url + "oauth/token",
            auth=(client_id, client_secret),
            data={"grant_type": "client_credentials"},
            headers=self.headers,
            timeout=(10, 20),
        )

        self.token = None
        if response.status_code == 200:
            self.token = response.json()["access_token"]

    def get_students(self):
        response = requests.get(
            self.base_url + "students/",
            headers={
                **self.headers,
                "Authorization": f"Bearer {self.token}",
            },
            timeout=(10, 20),
        )
        data = response.json()["items"]
        students = []
        for student in data:
            students.append([student["id"], student["name"]])
        return students

    def add_student(self,name):
        name = name.strip()
        if not name or len(name) > 100:
            raise ValueError("Enter a name between 1 and 100 characters.")

        # Insert the new student.
        response = requests.post(
            self.base_url + "students/",
            headers={
                **self.headers,
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
            json={"name": name},
            timeout=(10, 20),
        )
        return response.status_code

"""
select * from DEMO_STUDENT;
insert into DEMO_STUDENT (NAME) values ('Derek');
"""



