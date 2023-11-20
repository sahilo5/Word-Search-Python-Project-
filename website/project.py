from flask import Blueprint, render_template, request
import requests

project = Blueprint('project', __name__)


@project.route('/', methods=['GET', 'POST'])
def index():
    return render_template("base.html")


@project.route('/search', methods=['GET', 'POST'])
def search():
    word = ""
    # word_title = ""

    if request.method == 'POST':
        word = request.form.get('word')

        fetch_info = Fetch_Info()
        word_title = fetch_info.fetch_word_title(word)
        word_defination = fetch_info.fetch_word_definations(word)
        word_Synonyms = fetch_info.fetch_word_Synonyms(word)
        word_Antonyms = fetch_info.fetch_word_Antonyms(word)

    return render_template("search.html", text=f"{word_title}", definations =word_defination, Synonyms=word_Synonyms, Antonyms=word_Antonyms)


class Fetch_Info:

    @staticmethod
    def fetch_word_title(word):
        try:
            response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
            response.raise_for_status()  # Raise an error for bad responses (e.g., 404)
            response_data = response.json()

            if response_data:
                result = response_data[0]["word"]
                return result
            else:
                return "Word not found"

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from the API: {e}")
            return "Word not found"

    @staticmethod
    def fetch_word_definations(word):
        try:
            response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
            response.raise_for_status()  # Raise an error for bad responses (e.g., 404)
            response_data = response.json()

            if response_data:
                
                result = response_data[0]["meanings"]
                list = []
                for defination in result[0]["definitions"]:
                    meaning =""
                    for means in defination['definition']:
                        meaning += means 

                    list.append(meaning)
                return list
            else:
                return "Word not found"
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from the API: {e}")
            return "Word not found"
            

    @staticmethod
    def fetch_word_Synonyms(word):
        try:
            api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
            response = requests.get(api_url, headers={'X-Api-Key': 'b/a1miBFuYUoVT5e91ZcCQ==aY8DPeC0KTpVFdsW'})
            if response.status_code == requests.codes.ok:
                response_data = response.json()
                synonyms_list = []
                for synonym in response_data["synonyms"]:
                    synonyms_list.append(synonym)
                
                return synonyms_list
            else:
                return "Word not found"


        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from the API: {e}")
            return "Word not found"

    @staticmethod
    def fetch_word_Antonyms(word):
        try:
            api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
            response = requests.get(api_url, headers={'X-Api-Key': 'b/a1miBFuYUoVT5e91ZcCQ==aY8DPeC0KTpVFdsW'})
            if response.status_code == requests.codes.ok:
                response_data = response.json()
                antonyms_list = []
                for synonym in response_data["antonyms"]:
                    antonyms_list.append(synonym)
                print(antonyms_list)
                return antonyms_list
            else:
                return "Word not found"


        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from the API: {e}")
            return "Word not found"

if __name__ == '__main__':
    from flask import Flask

    app = Flask(__name__)
    app.register_blueprint(project)

    app.run(debug=True)
