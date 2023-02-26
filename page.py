from chrumium import BrowserModule
browser = BrowserModule()

class Control:
    def __init__(self, title="Document"):
        self._head = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>{title}</title>\n</head>\n<body>\n'
        self._body = '\n</body>\n</html>'
        self.head_content = ""
        self.body_content = ""
        self.html_tags = []

    @property
    def head(self):
        return self._head.format(title=self.title)

    @property
    def body(self):
        return self._body

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def get_html(self):
        tags = '\n'.join(self.html_tags)
        return self.head + self.head_content + self.body_content + tags + self.body


doc = Control()
doc.head_content = '<style>button {color: blue;}</style>'
doc.body_content = '<button>Hello</button>'
doc.title = 'My Document'
doc.html_tags.append('<p>This is a paragraph.</p>')
doc.html_tags.append('<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>')
doc.html_tags.append('<input type="text>')
html_doc = doc.get_html()



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