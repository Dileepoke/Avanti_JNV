import urllib.request
import webbrowser

sub = ''
choice = int(
    input(
        "Select Subject \n1.Mathematics \n2.Biology \n3.Physics \n4.Chemistry \n"
        'Enter Subject Number:'))
if choice == 1:
    sub = "https://lnk.avantifellows.org/XIENABLEMATH"
elif choice == 2:
    sub = "https://lnk.avantifellows.org/XIENABLBIO"
elif choice == 3:
    sub = "https://lnk.avantifellows.org/XIENABLEPHY"
elif choice == 4:
    sub = "https://lnk.avantifellows.org/XIENABLECHEM"
else:
    print("\n\n\n\nChoice only 1 to 4 options only")

x = urllib.request.urlopen(sub)
url = x.url.split('&')[2].split('=')[1]
yt = 'https://youtu.be/' + url
print(yt)
webbrowser.open_new_tab(yt)
