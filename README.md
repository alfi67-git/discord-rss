# Send RSS messages in a Discord channel
This script allow you to connect to an RSS feed, and every times it actualising, a new message is sent on the selected channel.

## Setup and Execution

### Prerequisites

- Python 3.6 or higher

### Steps

1. Clone this repo :

    ```sh
    git clone https://github.com/alfi67-git/discord-rss
    cd discord-rss
    ```

2. Go in main.py and specifie :
    - The webhook bot url
    - The name of the bot
    - The url of the rss feed

3. For Linux/macOS :

    ```sh
    ./setup.sh
    ```

4. For Windows :

    ```bat
    setup.bat
    ```

These scripts will create a virtual environment, install the necessary dependencies, and run the main script.
