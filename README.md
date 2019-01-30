# cryptopanic_API_Wrapper

Simple Wrapper to help pull data from the cryptopanic API.

**api_gather.py** Contains functions to make calls to cryptopanic API easier. *Hopefully.*

**format.py** Contain a basic layout of how to use calls, and format the data into a pandas df.

The purpose of this wrapper is to enable functional integration with the cryptopanic API. Further, format the responses to aid in a crypto NLP system.

To run:
 *  Clone the repo on your local machine. `$ git clone https://github.com/GrilledChickenThighs/cryptopanic_API_Wrapper.git`
 *  Navigate to the project directory
 *  Run `$ python3 setup.py`
 *  Make an API Auth Token by signing up on cryptopanic.com
 *  Copy your new API token
 *  Open config.py and paste your Token into the API_KEY field
 
