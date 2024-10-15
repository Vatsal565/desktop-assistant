## Voice Assistant

Welcome to the Voice Assistant repository! This project houses a Python script designed to act as a basic voice-controlled assistant, leveraging several libraries to enable various functionalities. Whether you're curious about its inner workings or eager to utilize its capabilities, this guide will provide you with all the necessary information to get started.

### Overview

The Voice Assistant is an interactive Python script that allows users to perform tasks using voice commands. Built using libraries like `pyttsx3`, `speech_recognition`, `wikipedia`, `webbrowser`, and `smtplib`, this assistant provides a seamless and hands-free user experience. From searching for information on Wikipedia to controlling web browsers and sending emails, the assistant offers a diverse range of features to assist users in their daily tasks.

### Features

#### Voice Recognition
At the core of the Voice Assistant is its ability to recognize voice commands. By leveraging the `speech_recognition` library, the assistant listens to user input through the microphone and converts it into text, enabling seamless interaction.

#### Wikipedia Search
Users can ask the assistant to search for information on Wikipedia by simply stating their query. The assistant then retrieves relevant summaries from Wikipedia articles, providing users with quick access to information on a wide range of topics.

#### Web Browsing
With the capability to open web browsers and navigate to specific websites, the assistant enables users to browse the internet hands-free. Whether it's accessing Google for search queries or visiting social media platforms like YouTube and Instagram, users can command the assistant to perform these tasks effortlessly.

#### Music Player
The Voice Assistant doubles as a music player, allowing users to enjoy their favorite tunes with voice commands. By specifying the command to play music, the assistant randomly selects songs from a predefined directory and starts playback, providing users with an enjoyable listening experience.

#### Email Sending
Sending emails becomes a breeze with the Voice Assistant. Users can instruct the assistant to compose and send emails to predefined contacts. By providing the recipient's name, along with the subject and content of the email, users can efficiently communicate without needing to type or access their email client manually.

#### Time Reporting
Need to know the current date and time? Simply ask the Voice Assistant, and it will promptly provide the information. This feature enables users to stay updated on the time without having to check their devices manually.

#### App Control
The assistant offers basic application control functionalities, allowing users to close web browsers and stop music playback as desired. This feature enhances the user's ability to manage their digital environment using voice commands.

### Setup

To set up the Voice Assistant on your system, follow these steps:

1. **Dependencies Installation**: Ensure Python is installed on your system, and install the required libraries using pip. Run the following command:
    ```
    pip install pyttsx3 datetime speech_recognition wikipedia smtplib
    ```

2. **Configuration**: Update the `GMAIL_ID` and `GMAIL_PASS` variables with your Gmail credentials. Additionally, customize the contacts dictionary with the email addresses of your desired recipients.

3. **Path Configuration**: Adjust paths for web browsers, music directories, and any other applications to match your system setup.

### Usage

To use the Voice Assistant:

1. Run the script `voice_assistant.py`.
2. Upon execution, the assistant will greet you based on the time of day.
3. Begin issuing voice commands prefixed with "Hey bot" to interact with the assistant.

### Conclusion

The Voice Assistant project aims to enhance user productivity and convenience by providing a versatile and intuitive interface for performing various tasks using voice commands. Whether you're a tech enthusiast exploring the capabilities of voice recognition or someone looking for practical solutions to streamline daily activities, the Voice Assistant offers a compelling solution.

### Disclaimer

While the Voice Assistant strives to provide a reliable and efficient user experience, it may encounter limitations or unforeseen issues in certain scenarios. Users are advised to use the assistant responsibly and understand that it may require further refinement for optimal performance in all use cases.
