# imports
import openai

# bot class
class ChatBot:
    def __init__(self):
        # set the api key
        openai.api_key  = '' #XXX this will be empty so put your own api key but in the ready apps it is set up but here it isn't for security reasons
    def get_response(self,user_input):
        # Return Bot Response
        return openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
