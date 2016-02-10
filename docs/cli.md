# Juice : Command Line Tool

Juice comes with a command line interface to conveniently create projects, 
build assets, push assets to S3, deploy application to production server and more.

There two types of command line tool. 
 
`juice`: The command to let you create projects,  build assets, 
push assets to S3, deploy application to production server and more 

`juice:cli` [juice:cli](application/cli.md) to manage your own command line interface

Below are the availale commands for `juice`

---

## create

To create new project in your application.

    juice create www
    
*Where `www` is the $project_name.*

**arguments**

- $project_name : The name of the project to create
    
**options**

- --skel | -s *(default: app)* - The pre-made skeleton to use for the project. 
    - `app` : Basic skeleton
    - `api` : A skeleton for RESTful API



Create a project named `api` with `api` skeleton

    juice create api --skel api

    
---

## serve

Allows to launch a project in local dev environment.

    juice serve www

*Where `www` is the $project_name.*

**arguments**

- $project_name : The name of the project to serve
    
**options**

- -p | --port *(default: 5000)* - The port to use if you want to use one other than 5000

- --no-watch - The name of the project to create. 
No space or dashes.


This will launch the `www` project under port 5001

    juice serve www -p 5001


To not watch the files when serving, so it doesn't reload

    juice serve api --no-watch 1
    
---

## buildassets

Allows to build web assets static files for the project

    juice buildassets www
    
*Where `www` is the $project_name.*

**arguments**

- $project_name : The name of the project
    
---

## assets2s3

If you want to host your assets on AWS S3, **juice** can conveniently upload 
them on S3.

    juice assets2s3 www
    
*Where `www` is the $project_name.*

**arguments**

- $project_name : The name of the project
    
    
By default the `Development` config will be used. 
If you want to use the `PRODUCTION` to upload from your local machine:

    ENV='PRODUCTION' juice assets2s3 -p www

---

## push

This is convenient command to push your application to production server by using GIT.

    juice push web 

*Where `web` is the $remote_name.*

No need to add a remote manually. By specifying the remote in your `propel.yml`
file, it will push it to that remote. This will allow to quickly change the remotes
to push to. Of course you must commit your code.

**arguments**

- $remote_name : The name of the remote in propel.yml to push
    
    
**options**

- --all : To push to all remotes

In your `/propel.yml` file, edit the section `git-remotes`:


    git-remotes:
      web:
        - ssh://user@host/path.git
        - ssh://user@host2/application-name.git
      workers:
        - ssh://user@host3/another.git

Now to push to `web` only:

    juice push web

To push `workers`:

    juice push workers
    
To push to all remotes:

    juice push --all




