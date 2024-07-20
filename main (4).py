import requests
import time
from datetime import datetime
#Discord webhooks
Snippet_Main = "PUT_YOUR_WEBHOOK_HERE"
Snippet_Logs = "PUT_YOUR_WEBHOOK_HERE"
Session_Ticket = "PUT_YOUR_WEBHOOK_HERE"
#Variables
regions = ["US", "USW", "EU"]
title = "63FDD"
FingerPainter = "LBADE."
Stick = "LBAAK."
Admin = "LBAAD."
HighTech = "LMAAV."
UnreleasedSweater = "LBACP."
IllustratorBadge = "LBAGS. "

#Ingame codes
Codes = [
    "JMAN",
    "ZERDY",
    "DAPPER",
    "SNAIL",
    "ELLIOT",
    "K9",
    "TURBO",
    "VMT",
    "MOSA",
    "RAKZZ",
    "MAXO",
    "AUSSIE",
    "DAPPERSLUG",
    "TYLERVR",
    "STYLEDSNAIL",
    "CODY",
    "QUINN",
    "LEOVR",
    "LEO",
    "PARTYMONKEY",
    "BOETHIA",
    "CHIVI",
    "HEADCHEF",
    "HEADCHEFVR",
    "KNINLY",
    "JAWCLAMPS",
    "MAJORA",
    "KISHARK",
    "WIDDOM",
    "TIKTOK",
    "TTT",
    "DAISY",
    "J3VU",
    "RUN",
    "SREN17",
    "YOUTUBER",
    "GTC",
    "K9",
    "MODS",
    "GTC1",
    "GTC2",
    "GTC3",
    "GTC4",
    "GTC5",
    "GTC6",
    "GTC7",
    "GTC8",
    "GTC9",
    "GTC10",
    "O",
    "PIG",
    "TTTPIG",
    "LEMMING",
    "AA",
    "JUAN",
    "THUMBZ",
    "VMT",
    "TYLERVR",
    "A",
    "JMAN1",
    "ELLIOT",
    "K8",
    "TIMMY",
    "JMAN2",
    "JMAN3",
    "GT",
    "CGT",
    "GTC",
    "GHOST",
    "DAISY09",
    "RUN",
    "RUN1",
    "666",
    "DAISY099",
    "ENDISHERE",
    "ECHO",
    "CHIPPD",
    "BANJO",
    "CHIPPDBANJO",
    "GH0ST",
    "END",
    "DEATH",
    "FNAF",
    "GTAG",
    "ECH0",
    "BANANA",
    "SMILER",
    "UNKNOWN",
    "BOTS",
    "DEAD",
    "HUNT",
    "J3VU",
    "MORSE",
    "PBBV",
    "SPIDER",
    "SREN17",
    "SREN18",
    "MONK",
    "STATUE",
    "GORILLA",
    "LEMMING",
    "STICK",
    "MODDER",
    "MODDERS",
    "MODERATOR",
    "TTTPIG",
    "ANTOCA",
    "BODA",
    "JOLYENE",
    "ELECTRONIC",
    "OWNER",
    "DEV",
    "CREATOR",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "CREEP",
    "CREEPY",
    "SCARY",
    "SPOOKY",
    "SPOOK",
    "MINIGAMES",
    "GAMES",
    "PLAY",
    "FINGERPAINTER",
    "CONTENTCREATOR",
    "CONTENT",
    "MIRRORMAN",
    "HELPME",
    "BEES",
    "NAMO",
    "WARNING",
    "BANSHEE",
    "JUAN",
    "THUMBZ",
    "VMT",
    "TYLERVR",
    "PARTYMONKEY",
    "HIDE",
    "MONKEY",
    "WOW",
    "THUMBZ",
    "MITTENS",
    "RAY2",
    "RAY1",
    "GRAPES",
    "MICROPHONE",
    "BARK",
    "DURF",
    "JULIAN",
    "HAVEN",
    "PIG",
    "TTTPIG",
    "VR",
    "WEAREVR",
    "GTAG",
    "GORILLA",
    "GT",
    "MOD",
    "MODS",
    "FINGER",
    "PAINTER",
    "STICK",
    "ADMIN",
    "STAFF",
    "STYLED",
    "SNAIL",
    "JUAN",
    "CRASH",
    "AUSSIE",
    "YOUTUBE",
    "TIKTOK",
    "MODDER",
    "MODDING",
    "GTC",
    "K9",
    "JMAN",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "O",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "ALEC",
    "ALECVR",
]

#Send notification to webhook saying tracker started
def Tracker_Started(user):
    print (f"Player tracker started by {user}")
    current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = {
        "content":
        "<@&BUYER_ROLE_ID>",
        "embeds": [{
            "title": f"Player Tracker Started",
            "description":
            f"**{user}** has started the tracker. Have fun tracking!",
            "color": 0x00FFFFFF,
            "footer": {
                "text": "Log generated at"
            },
            "author": {
                "name":
                "Player Tracker",
                "icon_url":
                "https://media.discordapp.net/attachments/1264063932507885638/1264063952447471626/aa27eef2b9f84e48b30d4e4a2db7ca1c.jpg?ex=669c82cb&is=669b314b&hm=010bad4b6d460661dbcaa14a79a7da748401447e27c55bf5e0f7bf6df9237fc9&=&format=webp&width=898&height=4096",
            },
            "thumbnail": {
                "url":
                "https://media.discordapp.net/attachments/1264063932507885638/1264063952447471626/aa27eef2b9f84e48b30d4e4a2db7ca1c.jpg?ex=669c82cb&is=669b314b&hm=010bad4b6d460661dbcaa14a79a7da748401447e27c55bf5e0f7bf6df9237fc9&=&format=webp&width=898&height=4096"
            },
            "timestamp": f"{current_time}",
        }]
    }
    response = requests.post(Snippet_Main, json=payload)
    if response.status_code != 204:
        print(
            f"Failed to send log to webhook. Status code: {response.status_code}"
        )


def successful_log(login_response):
    current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = {
        "embeds": [{
            "title": "Session Ticket Status",
            "description":
            f"**Sucessfuly Fetched Session Ticket**\n{login_response}",
            "color": 0x00FF00,
            "footer": {
                "text": "Log generated at"
            },
            "author": {
                "name":
                "Snippet Tracker",
                "icon_url":
                "https://media.discordapp.net/attachments/1264063932507885638/1264063952447471626/aa27eef2b9f84e48b30d4e4a2db7ca1c.jpg?ex=669c82cb&is=669b314b&hm=010bad4b6d460661dbcaa14a79a7da748401447e27c55bf5e0f7bf6df9237fc9&=&format=webp&width=898&height=4096",
            },
            "thumbnail": {
                "url":
                "https://media.discordapp.net/attachments/1264063932507885638/1264063952447471626/aa27eef2b9f84e48b30d4e4a2db7ca1c.jpg?ex=669c82cb&is=669b314b&hm=010bad4b6d460661dbcaa14a79a7da748401447e27c55bf5e0f7bf6df9237fc9&=&format=webp&width=898&height=4096"
            },
            "timestamp": f"{current_time}",
        }]
    }
    response = requests.post(Session_Ticket, json=payload)
    if response.status_code != 204:
        print(
            f"Failed to send log to webhook. Status code: {response.status_code}"
        )


def error_log(login_response):
    print(f"Session Ticket Was Invalid \n{login_response}")
    current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = {
        "content":
        "@everyone",
        "embeds": [{
            "title": "Session Ticket Status",
            "description":
            f"**Error Fetching Session Ticket** \n{login_response}",
            "color": 0xFF0000,  # Red color
            "footer": {
                "text": "Log generated at"
            },
            "author": {
                "name":
                "Player Tracker",
                "icon_url":
                "https://cdn.discordapp.com/avatars/660173171219103776/a_4cf76c60f02f4b457dd401297feebb68.gif?size=4096",
            },
            "thumbnail": {
                "url":
                "https://tenor.com/view/horror-halloween-michael-myers-scream-ghostface-gif-4184100939481253080"
            },
            "timestamp": f"{current_time}",
        }]
    }
    response = requests.post(Session_Ticket, json=payload)
    if response.status_code != 204:
        print(
            f"Failed to send log to webhook. Status code: {response.status_code}"
        )


def Player_Found(item, room, count):
    print(f"FOUND A {item} IN ROOM {room}")
    current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = {
        "content":
        "<@&BUYER_ROLE_ID>",
        "embeds": [{
            "title": f"FOUND A: **{item}**",
            "description":
            f"**ITEM: {item}** 
            ROOM: **{room}** 
            TIME: {current_time} ",
            "color": 0x00FF00,
            "footer": {
                "text": "Log generated at"
            },
            "author": {
                "name":
                "Player Traker Log",
                "icon_url":
                "https://media.discordapp.net/attachments/1264063932507885638/1264063952447471626/aa27eef2b9f84e48b30d4e4a2db7ca1c.jpg?ex=669c82cb&is=669b314b&hm=010bad4b6d460661dbcaa14a79a7da748401447e27c55bf5e0f7bf6df9237fc9&=&format=webp&width=898&height=1082"
            },
            "thumbnail": {
                "url":
                "https://media.discordapp.net/attachments/1264063932507885638/1264063952447471626/aa27eef2b9f84e48b30d4e4a2db7ca1c.jpg?ex=669c82cb&is=669b314b&hm=010bad4b6d460661dbcaa14a79a7da748401447e27c55bf5e0f7bf6df9237fc9&=&format=webp&width=898&height=1082"
            },
            "timestamp": f"{current_time}"
        }]
    }
    response = requests.post(Snippet_Main, json=payload)
    if response.status_code != 204:
        print(
            f"Failed to send log to webhook. Status code: {response.status_code}"
        )


def Player_Missed(code, data):
    print(f"Code: '{code}' was checked and had no special cosmetics \n All cosemtics in room: \n {data} ")
    current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = {
        "embeds": [{
            "title": "Tracker didn't find Special Players!",
            "description":
            f"**Code: '{code}' had no special cosmetics** \n *All cosmetics in room:* \n {data}",
            "color": 0xFF0000,
            "footer": {
                "text": "Log generated"
            },
            "author": {
                "name":
                "Player Log",
                "icon_url":
                "https://media.discordapp.net/attachments/1264063932507885638/1264063952447471626/aa27eef2b9f84e48b30d4e4a2db7ca1c.jpg?ex=669c82cb&is=669b314b&hm=010bad4b6d460661dbcaa14a79a7da748401447e27c55bf5e0f7bf6df9237fc9&=&format=webp&width=898&height=1082"
            },
            "thumbnail": {
                "url":
                "https://media.discordapp.net/attachments/1264063932507885638/1264063952447471626/aa27eef2b9f84e48b30d4e4a2db7ca1c.jpg?ex=669c82cb&is=669b314b&hm=010bad4b6d460661dbcaa14a79a7da748401447e27c55bf5e0f7bf6df9237fc9&=&format=webp&width=898&height=1082"
            },
            "timestamp": f"{current_time}"
        }]
    }
    response = requests.post(Snippet_Logs, json=payload)
    if response.status_code != 204:
        print(
            f"Failed to send log to webhook. Status code: {response.status_code}"
        )


def send_webhook_embed_log(title, Color, message, webhook):
    current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = {
        "embeds": [{
            "title": title,
            "description": message,
            "color": Color,
            "author": {
                "name":
                "Log Assistant",
                "icon_url":
                "https://media.discordapp.net/attachments/1264063932507885638/1264063952447471626/aa27eef2b9f84e48b30d4e4a2db7ca1c.jpg?ex=669c82cb&is=669b314b&hm=010bad4b6d460661dbcaa14a79a7da748401447e27c55bf5e0f7bf6df9237fc9&=&format=webp&width=898&height=1082"
            },
            "footer": {
                "text": "Log generated at"
            },
            "thumbnail": {
                "url":
                "https://media.discordapp.net/attachments/1264063932507885638/1264063952447471626/aa27eef2b9f84e48b30d4e4a2db7ca1c.jpg?ex=669c82cb&is=669b314b&hm=010bad4b6d460661dbcaa14a79a7da748401447e27c55bf5e0f7bf6df9237fc9&=&format=webp&width=898&height=1082"
            },
            "timestamp": f"{current_time}"
        }]
    }
    response = requests.post(webhook, json=payload)
    if response.status_code != 204:
        print(
            f"Failed to send log to webhook. Status code: {response.status_code}"
        )


def send_webhook_log(message, webhook):
    payload = {"content": message}
    response = requests.post(webhook, json=payload)
    if response.status_code != 204:
        print(
            f"Failed to send log to webhook. Status code: {response.status_code}"
        )


def get_session_ticket(steamticket):
    login = requests.post(
        url=f"https://{title}.playfabapi.com/Client/LoginWithSteam",
        json={
            "SteamTicket": steamticket,
            "CreateAccount": True,
            "TitleId": title,
        },
    )
    loginresponse = login.json()
    if "data" in loginresponse and "SessionTicket" in loginresponse["data"]:
        return loginresponse
    else:
        error_log(loginresponse)
        print("Error fetching session ticket:")
        print(loginresponse)
        return None


def check_data(session_ticket):
    ClientHeaders = {"X-Authorization": session_ticket}
    for word in Codes:
        for region in regions:
            combined_code = word + region
            Keys = ""
            request = {
                "SharedGroupId": combined_code,
                "GetMembers": True,
                "Keys": Keys,
            }
            createshared = requests.post(
                url=f"https://{title}.playfabapi.com/Client/GetSharedGroupData",
                json=request,
                headers=ClientHeaders,
            )
            response_data = createshared.json()
            count = "0/0"
            if "data" in response_data and FingerPainter in str(
                    response_data["data"]):
                # last param is player room count
                Player_Found("FINGER PAINTER", word, count)
            if "data" in response_data and HighTech in str(
                    response_data["data"]):
                Player_Found("HIGHTEC SLINGSHOT", word, count)
            if "data" in response_data and Stick in str(response_data["data"]):
                Player_Found("STICK", word, count)
            if "data" in response_data and Admin in str(response_data["data"]):
                Player_Found("ADMIN BADGE", word, count)
            if "data" in response_data and UnreleasedSweater in str(
                    response_data["data"]):
                Player_Found("UnreleasedSweater", word, count)
            if "data" in response_data and IllustratorBadge in str(
                    response_data["data"]):
                Player_Found("IllustratorBadge", word, count)
            else:
                Player_Missed(combined_code, response_data)
                print(
                    f"Did not find '{combined_code}' or encountered an error. Response:"
                )
                print(response_data)

            time.sleep(0.3)


def format_account_info_message(account_info):
    formatted_message = (
        f"**DisplayName:** {account_info['DisplayName']}\n"
        f"**PlayerId:** {account_info['PlayerId']}\n"
        f"**Email:** {account_info['Email']}\n"
        f"**Banned:** {account_info['IsBanned']}\n"
        f"**LastLoginDate:** {account_info['LastLoginDate']}\n"
        f"**CreationDate:** {account_info['CreationDate']}\n")
    return formatted_message


def get_account_info(session_ticket, playfab_id):
    ClientHeaders = {"X-Authorization": session_ticket}
    request = {"PlayFabId": playfab_id}

    account_info_response = requests.post(
        url=f"https://{title}.playfabapi.com/Client/GetAccountInfo",
        json=request,
        headers=ClientHeaders,
    )

    response_data = account_info_response.json()
    account_info = response_data.get("data", {}).get("AccountInfo", {})
    creation_date = account_info.get("Created", "N/A")
    last_login_date = account_info.get("LastLogin", "N/A")
    player_id = account_info.get("PlayFabId", "N/A")
    is_banned = account_info.get("BannedUntil", None) is not None
    display_name = account_info.get("TitleInfo", {}).get("DisplayName", "N/A")
    email = account_info.get("PrivateInfo", {}).get("Email", "N/A")

    return {
        "CreationDate": creation_date,
        "LastLoginDate": last_login_date,
        "PlayerId": player_id,
        "IsBanned": is_banned,
        "DisplayName": display_name,
        "Email": email,
    }


def main():

    user = input("User: ")
    steamticket = input("Ticket: ")
    Tracker_Started(user)

    while True:
        loginresponse = get_session_ticket(steamticket)
        if loginresponse:

            successful_log(loginresponse)
            session_ticket = loginresponse["data"]["SessionTicket"]
            playfab_id = loginresponse["data"]["PlayFabId"]
            account_info = get_account_info(session_ticket, playfab_id)
            formatted_message = format_account_info_message(account_info)
            send_webhook_embed_log("Account Information", 0x00FF00,
                                   formatted_message, Session_Ticket)

            check_data(session_ticket)
        else:
            print("Failed to obtain session. Retrying...")
            time.sleep(60)


if __name__ == "__main__":
    main()
