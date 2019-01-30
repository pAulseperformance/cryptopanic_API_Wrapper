import webbrowser

webbrowser.open('https://cryptopanic.com/developers/api/')

f = open("config.py","w+")
f.write("API_KEY = '<yourapikeyhere>'")
