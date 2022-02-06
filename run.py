from v0coderapp import app
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
if __name__ == '__main__':
    app.run(debug=True)
