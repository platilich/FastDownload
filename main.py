import asyncio
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button, Input
from textual.containers import HorizontalGroup, VerticalScroll
from download_video import download_youtube


class Main(HorizontalGroup):

    def compose(self) -> ComposeResult:
        yield Input(placeholder='Enter the url of video', id='input')
        yield Button(label='Download', id='download')


class FastDownload(App):

    BINDINGS = [('d', 'toggle_dark', 'Toggle dark mode')]


    CSS_PATH = 'main.tcss'


    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield VerticalScroll(Main())




    def action_toggle_dark(self) -> None:
        if self.theme == 'textual-light':
            self.theme = 'textual-dark'

        elif self.theme == 'textual-dark':
            self.theme = 'textual-light'




    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id != 'download':
            self.notify(message='игнор', title='win')
            return


        video_url = str(self.query_one('#input', Input).value.strip())




        if video_url is None:
            self.notify(message='Input url is empty', title='FastDownload')
            return

        result = await asyncio.to_thread(download_youtube, video_url)

        if result:
            self.notify(message='Готово, видео скачалось!', title='FastDownload')

        else:
            self.notify(message='Что-то пошло не так', title='FastDownload')






if __name__ == '__main__':
    app = FastDownload()
    app.run()
