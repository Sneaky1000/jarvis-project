from jarvis.audio.listener import AudioListener

def main():
    listener = AudioListener()
    try:
        while True:
            command = listener.listen()
            if command:
                print("You said:", command)
    except KeyboardInterrupt:
        print("\nExiting on Ctrl+C")

if __name__ == "__main__":
    main()
