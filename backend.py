import openai


class ChatBot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003"
            prompt = user_input
            max_tokens = 3000
            temperature = 0.5
            # varies from 0 to 1
            # higher temperature ---> lower accuracy
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("Write a joke about birds")
    print(response)