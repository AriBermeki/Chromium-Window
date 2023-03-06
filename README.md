# Python-Chromium
### lettl Widght like Chromium Widght based on Chrome

<p>Installation</p>

```bash
python3 -m pip install hybrid-chromium
```

## Usage

Write your nice GUI in a file `main.py`:

```python
from chromium import BrowserModule

#Open the browser in full screen mode
BrowserModule.browser_open(url='https://example.com', fullscreen=True)

#Open the browser in dark mode
BrowserModule.browser_open(view='app', url='https://example.com', width=800, height=600, darck_modo=True)


```



