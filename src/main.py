import textual.app as txa
import textual.widgets as txw
from household import Household, Level, LowerClass, MiddleClass, UpperClass
from random import randint

class App(txa.App):
    def compose(self) -> txa.ComposeResult:
        yield txw.Header()   
        yield txw.DataTable(id='data')
        yield txw.Footer()  

    def on_mount(self):
        pass

if __name__ == '__main__':
    # Create our households real quick
    households: list[Household] = []
    for i in range(0, 10):
        level: Level = {
            1: LowerClass,
            2: MiddleClass,
            3: UpperClass
        }[randint(1, 3)]
        h = Household(level())
        h.introduce()
        households.append(h)
    
    #app = App()
    #app.run()