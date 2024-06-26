import aiohttp
import urllib.parse

apikey = "43693facbb24d1ac893a7d33846b15cc"


async def gettrackplaycount(user: str, track: dict) -> int:
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={apikey}&artist={track['artist']['#text']}&track={urllib.parse.quote(track['name'].lower())}&format=json&username={user}"
        ) as r:
            data = await r.json()
            return data["track"]["userplaycount"]


# from track
async def getalbumplaycount(user: str, track: dict) -> int:
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={apikey}&artist={track['artist']['#text']}&album={track['album']['#text']}&format=json&username={user}"
        ) as r:
            data = await r.json()
            return data["album"]["userplaycount"]


# from track
async def getartistlaycount(user: str, track: dict) -> int:
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://ws.audioscrobbler.com/2.0/?method=artist.getInfo&api_key={apikey}&artist={track['artist']['#text']}&format=json&username={user}"
        ) as response:
            r = await response.json()
            return r["artist"]["stats"]["userplaycount"]


# from track
async def getalbum(track: dict) -> dict:
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={apikey}&artist={track['artist']['#text']}&album={track['album']['#text']}&format=json"
        ) as response:
            r = await response.json()
            return r["album"]


async def gettrack(track: dict) -> dict:
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://ws.audioscrobbler.com/2.0/?method=track.getinfo&api_key={apikey}&artist={track['artist']['#text']}&track={track['track']['#text']}&format=json"
        ) as response:
            r = await response.json()
            return r


async def getui(user: str) -> dict:
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://ws.audioscrobbler.com/2.0/?method=user.getinfo&user={user}&api_key={apikey}&format=json"
        ) as response:
            r = await response.json()
            return r


async def gettopartists(user: str, count: int) -> dict:
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://ws.audioscrobbler.com/2.0/?method=user.getTopArtists&user={user}&api_key={apikey}&format=json&limit={count}"
        ) as response:
            r = await response.json()
            return r


async def gettracks(user: str, count: int) -> dict:
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={user}&api_key={apikey}&format=json&limit={count}"
        ) as r:
            response = await r.json()
            return response
