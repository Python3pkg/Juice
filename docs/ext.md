
## Flashing: 

### flash_success(), flash_error(), flash_info()

For convenience, you can use `flash_success()`, `flash_error()`, `flash_info()` 
to set flash message with category `success`, `error` and `info` respectively.

### flash_data(), get_flashed_data()

Similar to Flask's `flash()`, `flash_data()` stores data temporarily 
and pass it to the next request to be used once.

    my_data = {}
    flash_data(my_data)

To retrieve the data stored by `flash_data`, use `get_flashed_data()`. 
It can be accessed once, subsequent access will return `None` 

---

## Decorators


### login_required

This decorator is from flask_login, it ensures that the user is logged in and 
authenticated before having access to the enpoint

    from webmaster import Portfolio, login_required

    class Index(Portofolio):
        
        @login_required
        def secured(self):
            return self.render_()

### user_roles()

This decorator ensures that an authenticated user has one of the roles listed.

    from webmaster import Portfolio, user_roles

    class Index(Portofolio):
        
        @user_roles('ADMIN', 'SUPERADMIN')
        def secured(self):
            return self.render_()
            
### menu()



### route()

By default, the route is built on the method name of the class, to change the route


    from webmaster import Portfolio, route

    class Index(Portofolio):
        
        @route("")
        def hello_world(self):
            return self.render_()


### extends()

    from webmaster import Portfolio
    
    

    
---


# Extensions: webmaster.ext


## webmaster.ext.storage 


---

## webmaster.ext.cache 


---


## webmaster.ext.mailer 

---

## webmaster.ext.recaptcha 


---


## webmaster.ext.csrf 

---


## webmaster.ext.session 






