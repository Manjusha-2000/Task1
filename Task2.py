import speech_recognition as sr
import pyttsx3
import openai
from datetime import datetime

openai.api_key = "your-api-key-here"

engine = pyttsx3.init()

def speak(text):
    """Speak the given text aloud."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for user input and convert speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError:
            speak("Network error. Please try again.")
            return ""

def get_ai_response(command):
    """Get a response from OpenAI's GPT model."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful voice assistant."},
                      {"role": "user", "content": command}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return "Sorry, I am unable to respond at the moment."

def respond(command):
    """Define the assistant's responses."""
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "your name" in command:
        speak("I am your custom voice assistant.")
    elif "time" in command:
        speak(f"The time is {datetime.now().strftime('%I:%M %p')}")
    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        response = get_ai_response(command)  
        speak(response)

def main():
    speak("Starting your voice assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            respond(command)

if __name__ == "__main__":
    main()