# -*- coding: utf-8 -*-
{
    "name": "Hello World",
    "version": "1.0.0",
    "summary": "Simple test module that provides a Hello World model",
    "description": "A tiny module to test addon installation: model, views, menu, and access rights.",
    "author": "You",
    "license": "LGPL-3",
    "category": "Tools",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/hello_views.xml",
        "data/hello_demo.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
