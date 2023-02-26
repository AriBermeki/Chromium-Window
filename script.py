import json
import websocket


class JavaScript:
    def __init__(self, attributes=None, content=None, on_message=None):
        self.attributes = attributes or {}
        self.content = content or []
        self.on_message = on_message

        self.ws = None
        self.ws_url = None

    def __str__(self):
        attributes_str = " ".join([f"{key}='{value}'" for key, value in self.attributes.items()])
        content_str = "\n".join(self.content)
        return f"<script {attributes_str}>\n{content_str}\n</script>"

    def connect_websocket(self, url):
        self.ws_url = url
        self.ws = websocket.WebSocket(url, on_message=self._on_message)
        self.ws.run_forever()

    def send_function(self, func_name, args):
        data = {"function_name": func_name, "args": args}
        self.ws.send(json.dumps(data))

    def recive_function(self, ws, message):
        if self.on_message:
            self.on_message(json.loads(message))
