import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import requests
import json
from  pprint import pprint
r = requests.get("http://gimvicapp.404.si/data?addSubstitutions=true&classes[]=2B&snackType=navadna&lunchType=navadno")
json_data = r.content

data = json.loads(json_data)
dnevi = data["days"]


class HelloWorld(toga.App):
    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        # Create a main content box
        main_box = toga.Box(style=Pack(direction=COLUMN))
        for d in range(5):
            for i, l in enumerate(dnevi[d]["lessons"]):
                main_box.add(toga.Label(i+1, ":"))
                if len(l) == 0:
                    main_box.add(toga.Label("Ni"))
                    continue
                main_box.add(toga.Label(l["subjects"][0]))
                main_box.add(toga.Label(l["classrooms"][0]))
                main_box.add(toga.Label(l["teachers"][0]))
            
            main_box.add(toga.Label("Malca:", " -- ".join(dnevi[d]["snackLines"])))
            main_box.add(toga.Label("Kosilo:", " -- ".join(dnevi[d]["lunchLines"])))
        container = toga.ScrollContainer(vertical=True)
        container.content = main_box


        # Add the content on the main window
        self.main_window.content = container

        # Show the main window
        self.main_window.show()


def main():
    return HelloWorld('Hello World', 'com.example.helloworld')
