
## Decorators


## @route(rule, \**kwargs)

**@route** has the same functionalities as Flask's route. The difference, it can be applied on the 
View class or methods in the View class

**Args**

- rule: (string - required) - The endpoint. ie: `/my-hello` 

- **kwargs:

    - endpoint (string - optional) - The endpoint name. Only on methods. ie: `CONTACT_US_PAGE`
    
    - defaults: (dict - optional) - To set defaults args. Only on methods. ie: `{'category': 'all'}`


on class View:

    from juice import View
    from juice.decorators import route
    
    @route("/my-hello")
    class Hello(View):
        
        def index(self):
            return {}

        def contact(self):
            return {}        

The above example have the following endpoints:

 `http://domain-name.com/my-hello` and `http://domain-name.com/my-hello/contact`
    

on View action:

    class World(View):
        
        def index(self):
            return {}   
             
        @route("/contact-us")
        def contact(self):
            return {}

The above example have the following endpoints:

 `http://domain-name.com/world` and `http://domain-name.com/world/contact-us`

---

## @menu(name, **kwargs)

@menu lets you conveniently create a Menu navigation on the View class and actions. 

It can be used in the template to create a navigation menu effortlessly without editing any HTML.

The menu can be ordered and placed anywhere on the page. 

With this method you can show and hide the menu without even touching any HTML. 


**Args**

- name: The menu name

- **kwargs:

    - order (int) : The order of the menu in the list.

    - visible (bool or callback) : To hide/show menu
    
    - endpoint (string): By default the endpoint is built based on the method and class.
     When set it will be used instead
    
    - endpoint_kwargs (dict): dict of k/v data for enpoint

    - group_name (string): On class menu, it can be used to filter a menu set to display. 
    If a class is passed, it will try to inherit the group from that class
    
    - url (string): To override the normal `endpoint` and use a URL 
    
    - target (string): to use along with url, if applying a different target. ie: _blank
    
    - align_right (bool): By default it assumes the menu is on the left, 
    when True it will set the flag for right
    
    - fa_icon (bool): The font-awesome icon to use. ie: fa-pencil
    
    - show_profile_avatar (bool): Show the profile avatar
    
    - show_profile_name (bool): Show profile name in the menu instead of menu title
    
    
    The args below will allow you to change where the menu is placed.
    By default they are set automatically

    - module_: the module name. Usually if using another module
    
    - class_: the class name class name in the module
    
    - method_: The method name, to build endpoint. Changing this will change the url
    
    - extends: class Name. To use the extends of the class


Example:

    @menu("Main Menu")
    class HelloWorld(View):
        
        @menu("Home")
        def index(self):
            return {}
            
        @menu("Password Checker")
        def check_password(view):
            return {}
                
---

## @methods(*args)

@methods allows to change the acceptable request method of a View Action. 

If the action is accessed with the wrong method, it will return a 403 Invalid Method

**Args**

- *args: POST, GET, PUT, DELETE 

Example:

    class HelloWorld(View):
        
        def index(self):
            return {}
            
        @methods('POST')
        def check_password(view):
            return {}
            
        @methods('POST', 'GET')
        def comments(self):
            if request.method == "GET":
                return {} 
                
            elif request.method == "POST":
                return {}

---

## @template


---

## @plugin



---

## @render_as_json

To render the view as JSON. The method must return a dict.

This decorator can be applied on the View class or the actions.

When applied on the View class, it will render all actions to JSON.

When applied on actions, only the action containing the decorator will be rendered as JSON.

On View class

    @render_as_json
    class API(View):
        
        def index(self):
            return {
                "version": 1,
                "name": "My API"
            }

On View action:

    class Index(View):
        
        def index(self):
            return {}
            
        @render_as_json
        def list_users(views):
            return {
                "users": [
                    "Mardix",
                    "Faby",
                    "Seba",
                    "Sami"
                ]
            }
            
---

## @render_as_xml

To render the view as XML. The method must return a dict.

This decorator can be applied on the View class or the actions.

When applied on the View class, it will render all actions to XML.

When applied on actions, only the action containing the decorator will be rendered as XML.

On View class

    @render_as_xml
    class API(View):
        
        def index(self):
            return {
                "version": 1,
                "name": "My API"
            }

On View action:

    class Index(View):
        
        def index(self):
            return {}
            
        @render_as_xml
        def list_users(views):
            return {
                "users": [
                    "Mardix",
                    "Faby",
                    "Seba",
                    "Sami"
                ]
            }
            
---

## @login_required

Extension of `flask_login.login_required` where it checks for the decorator 
`@no_login_required` in the same action. 
 
 If the View class has `login_required` as decorators, having `@no_login_required`
 on an action will not test if the act
 
 
 Example
 
    class Account(View):
        decorators = [login_required]
        
        def index(self):
            return {}
            
        @no_login_required
        def docs(self):
            return {}


With the above example, accessing `/account` will require login, but `/account/docs` 
will not require login.

---

## @fresh_login_required

Extension of `flask_login.fresh_login_required` where it checks for the decorator 
`@no_login_required` in the same action. 
 
 If the View class has `login_required` as decorators, having `@no_login_required`
 on an action will not test if the act
 
 
 Example
 
    class Account(View):
        
        @fresh_login_required
        def index(self):
            return {}
            
        @no_login_required
        def docs(self):
            return {}


With the above example, accessing `/account` will require fresh login, but `/account/docs` 
will not require login.

---

## @no_login_required

A dummy decorator that just stays there `@login_required` to skip login requirements 
on the method.

 Example
 
    class Account(View):
        decorators = [login_required]
        
        def index(self):
            return {}
            
        @no_login_required
        def docs(self):
            return {}


With the above example, accessing `/account` will require login, but `/account/docs` 
will not require login.

---

## @require_user_roles(*roles)

A decorator to check if user has any of the roles specified


**Args**

- *roles: tuple of roles


Example:

    class Account(View):
        decorators = [login_required]
        
        def index(self):
            return {}

        @require_user_roles('superadmin', 'admin')
        def admin(self):
            return {}

        
---
