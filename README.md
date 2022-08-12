# GitHub Virtual Assistant

This project is a fully functional virtual assistant program that is targeted at answering GitHub's most frequently asked questions. There are many layers in the construction of the build including web scraping and data cleaning, a full neural network, and a built out frontend for a thourough user experience.

## Running the code yourself

In order to run this program, it is best to create a virtual environment before downloading packages and libraries, my personal choice was Anaconda (I will be using Anaconda syntax for examples, syntax may vary across programs). Once you have created the environment and activated it, you will need to download the following packages to run the main program.
```
conda install Flask, flask-cors, torch, torchvision, nltk
```
You will also need to activate python and download a specific nltk package.
```
$ python3
>>> import nltk
>>> nltk.download('punkt')
```
Once this has been done, you can run the code yourself, starting with the train.py file. This will take in the dataset 'GitHub_FAQ.json' and train the neural net so that it is ready to chat (This should dump the saved model as model.pth). From here you are able to run the bot.py file, which is a fully functioning terminal based application for the chatbot. If you want to utilize the frontend for a better user experience, run the app.py file to start the flask app in the background. Then, with the help of the live server extension in VS Code, 'Go Live' from the base.html file. This should display the full user interface for the best interaction with the chatbot.

### Tips

This chatbot gives the best, most accurate responses to general questions about GitHub, such as the general purpose of the tool itself or other information that differentiates GitHub from its competition. Without copious amounts of public data, it may struggle to provide accurate answers to extremely specific questions.
