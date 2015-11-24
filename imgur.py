# -*- coding: utf-8 -*-
#
# Upload images to imgur for use in weechat
#
# Usage: /imgur PATH
#
# History:
#
# Version 1.0.0: initial release
#

import os
import os.path
import requests
import weechat

URL = "https://api.imgur.com/3/image"
CLIENT_ID = "client_id"


def get_client_id():
    imgur_token = weechat.config_get_plugin(CLIENT_ID)
    if imgur_token.startswith("${sec.data"):
        imgur_token = weechat.string_eval_expression(imgur_token, {}, {}, {})

    return imgur_token


def imgur(data, buf, args):
    filepath = os.path.expanduser(args)
    contents = open(filepath).read()
    files = {"image": contents}

    client_id = get_client_id()
    if len(client_id) == 0 or " " in client_id:
        raise Exception("Need to set imgur client id")

    headers = {"Authorization": "Client-ID %s" % client_id}
    response = requests.post(URL, files=files, headers=headers)
    data = response.json()
    image_url = data["data"]["link"]

    weechat.buffer_set(buf, "input", image_url)
    weechat.buffer_set(buf, "input_pos", str(len(image_url)))

    return weechat.WEECHAT_RC_OK


def main():
    if not weechat.register("imgur", "Keith Smiley", "1.0.0", "MIT",
                            "Upload an image to imgur", "", ""):
        return weechat.WEECHAT_RC_ERROR

    if not weechat.config_get_plugin(CLIENT_ID):
        weechat.config_set_plugin(CLIENT_ID, "Set imgur client ID")

    weechat.hook_command("imgur", "Pass the current buffer to urlview", "",
                         "", "filename", "imgur", "")

if __name__ == "__main__":
    main()
