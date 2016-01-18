
# Welcome to *Webmaster*


## 

    from webmaster import View
    from webmaster.decorators import menu
    
    class Index(View):
        
        @menu("Home")
        def index(self):
            return {}
            
        @menu("About Us")
        def about_us(self):
            return {}
            
---

## About

**WEBMASTER** is a Flask based web framework. 


---

For full documentation visit [mkdocs.org](http://mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs help` - Print this help message.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
