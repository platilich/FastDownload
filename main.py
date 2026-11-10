from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button, Input
from textual.containers import HorizontalGroup, VerticalScroll
from webbrowser import open



class Main(HorizontalGroup):

    def compose(self) -> ComposeResult:
        yield Input(placeholder='Enter the url of video', id='input')
        yield Button(label='Download', id='download')



class FastDownload(App):

    BINDINGS = [('d', 'toggle_dark', 'Toggle dark mode'), ('e', 'open', 'open chrome')]


    CSS_PATH = 'main.tcss'


    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield VerticalScroll(Main())




    def action_toggle_dark(self) -> None:
        self.theme = (
            'textual-dark' if self.theme == 'textual-light' else 'textual-dark'
        )


    def action_open(self) -> None:
        open('https://google.com')







if __name__ == '__main__':
    app = FastDownload()
    app.run()
