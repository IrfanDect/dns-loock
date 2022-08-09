import requests
from rich import print
from rich.panel import Panel
import subprocess
from rich.align import Align

banner = Align.center("""
┌┬┐  ┌┐┌  ┌─┐  ┬  ┌┐┌  ┌─┐  ┌─┐
 ││  │││  └─┐  │  │││  ├┤   │ │
─┴┘  ┘└┘  └─┘  ┴  ┘└┘  └    └─┘
        """)
def Main():
    subprocess.call('clear',shell=False)
    print(Panel(banner,border_style='blue bold'))
    ipn = input('\033[94;1mhostname :\033[97;1m ')
    url = f"http://api.hackertarget.com/dnslookup/?q={ipn}"
    req = requests.get(url)
    print(Panel(req.text,border_style='white bold',style='dim bold',highlight=True,title=" INFO "))

if __name__ == "__main__":
    Main()
