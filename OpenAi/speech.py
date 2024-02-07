import openai
import speech_recognition as sr

openai.api_key = "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"

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)

        # Use OpenAI GPT-3 to generate text from audio transcription
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Transcribe the following speech:\n{recognizer.recognize_google(audio_data)}",
            temperature=0.7,
            max_tokens=200
        )

        # Extract the transcribed text from the OpenAI response
        transcribed_text = response['choices'][0]['text']

        return transcribed_text

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except ValueError as ve:
        print(f"ValueError: {ve}. Please check if the audio file is in a supported format or if it's corrupted.")

if __name__ == "__main__":
    # Replace 'path/to/your/audiofile.mp3' with the actual path to your MP3 file
    audio_file_path = r'D:\Random_Ideas\OpenAi\speechEcho2.wav'  # Replace 'your_audio_file.mp3' with the actual file name

    transcribed_text = transcribe_audio(audio_file_path)

    if transcribed_text:
        print("Transcription:")
        print(transcribed_text)
