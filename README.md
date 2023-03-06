# Python-Chromium
A lettl Widght like Chromium Widght based on Chrome



from chrumium import BrowserModule



Öffne den Browser im Standardmodus mit der angegebenen URL
BrowserModule.browser_open(url='https://example.com')

Öffne den Browser im Vollbildmodus
BrowserModule.browser_open(url='https://example.com', fullscreen=True)

Öffne den Browser im App-Modus mit angegebener Größe und bestätige das Schließen
BrowserModule.browser_open(view='app', url='https://example.com', width=800, height=600, confirm_close=True)
