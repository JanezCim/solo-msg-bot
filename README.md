Simple bot that allows each user to post to specific channel in specific guild (aka server) in discord ONLY ONCE. If user deletes its message, they are allowed to post again.

Usage:

    cd PATH_TO_WORKSPACE
    nano env.sh

Insert inside 

    #.sh file
    export DISCORD_TOKEN="<insert_token_of_your_bot>"
    export DISCORD_GUILD="<insert_discord_guild_aka_server"
    export DISCORD_CHANNEL="<insert_discord_channel>"

you can get your bot token from https://discord.com/developers/applications

Then source it and run

    source env.sh
    python3 solo-msg-bot.py 