# imgur-weechat

This is a simple [weechat](https://weechat.org/) plugin that allows you
to upload images anonymously to [imgur](https://imgur.com/)

## Usage:

```
/imgur PATH_TO_FILE
```

## Configuration:

To use it you need to generate a client ID. You do that
[here](https://imgur.com/account/settings/apps).

```
# If you haven't already
/secure passphrase SECRET_PASSWORD
# Get this token here: https://imgur.com/account/settings/apps
/secure set imgur_token YOUR_TOKEN
/set plugins.var.python.imgur.client_id ${sec.data.imgur_token}
```

## Installation

Copy the script to `~/.weechat/python/autoload`

```sh
mkdir -p ~/.weechat/python/autoload
wget https://raw.githubusercontent.com/keith/imgur-weechat/master/imgur.py ~/.weechat/python/autoload
```
