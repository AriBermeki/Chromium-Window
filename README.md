# Python-Chromium
A lettl Widght like Chromium Widght based on Chrome



# from chrumium import BrowserModule


browser = BrowserModule()

def main(target: Control):
    url = "data:text/html," + target


    options = {
        '--app=': None,
        'app_mode': True,
        '--window-size=':None,
        '--remote-debugging-port=':True,
        '--app-window-icon=':None,
        '--app-window-size=':'1920x1080',
        '--no-sandbox': True,
        'cmdline_args': []
    }


    # Browserpfad finden
    path = browser.find_path()

    # Browser-Fenster öffnen
    browser.run(path, options, [url])

main(html_doc)
