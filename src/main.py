import textual.app as txa
import textual.widgets as txw
from household import Household
from expenses import LOWER_CLASS, MIDDLE_CLASS, UPPER_CLASS, Level, LEVEL_IDX
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
        level = LEVEL_IDX[randint(0, 2)]
        h = Household(level)
        h.introduce()
        households.append(h)
    
    app = App()
    app.run()