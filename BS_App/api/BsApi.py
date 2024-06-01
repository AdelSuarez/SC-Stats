import aiohttp
import BS_App.constants as constants

class BsApi:
    def __init__(self):
        self.base_url = "https://api.brawlstars.com/v1/players/%23"
        self.api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjIwY2ZiNTVhLTQyN2YtNGE2Yi05NmZkLTJlMWVlN2UxYzMwMCIsImlhdCI6MTcxNzIxNDA0Miwic3ViIjoiZGV2ZWxvcGVyL2FmODJlOTc2LWNmMmYtZDMxMC1iMjFhLWFjZTlhZGJhMTZiNiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTM4Ljg0LjQxLjIwMiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.YMU_ndTsU4owqtNVMKn0lPwZEH4avRlZbaAyyp5suXCFzWEfW7DU4ENMUWa6X22BV_-AXUkjBP0w1ETMfqxKoQ"

    async def get_player_info(self, player_tag):
        url = f"{self.base_url}{player_tag}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                elif response.status == 404:
                    return "void"
                elif response.status == 403:
                    return "error_api"
                else:
                    print(f"Error HTTP: {response.status}")

    async def get_icons(self):
        # URL base de la API
        base_url = 'https://api.brawlapi.com/v1'

        # Ruta para obtener íconos
        icons_endpoint = '/icons'

        async with aiohttp.ClientSession() as session:
            async with session.get(base_url + icons_endpoint) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error al obtener íconos. Código de estado: {response.status}")
