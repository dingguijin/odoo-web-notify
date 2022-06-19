# Copyright 2022 Guijin Ding, dingguijin@gmail.com

{
    "name": "Web Notify",
    "summary": """
    Send notification messages to internal user""",
    "version": "15.0",
    "license": "LGPL-3",
    "author": "Guijin Ding",
    "development_status": "Production/Stable",
    "website": "https://github.com/dingguijin/odoo-web-notify",
    "depends": ["web", "bus", "base"],
    "data": ["views/res_users.xml"],
    "demo": [],
    "assets": {
        "web.assets_backend": ['odoo-web-notify/static/src/js/notify.js']
    },
    "installable": True,
    "application": True
}
