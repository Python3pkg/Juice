# Juice : Command Line Tool

**juice** is a command line tool to conveniently create projects, 
build assets, push assets to S3, deploy application to production server and more.

**juice** was created during the installation of Juice.

Below are the availale commands:

---

## create

To create new project in your application.

**Args**

- --project | -p *(required. default: www)* - The name of the project to create. 
No space or dashes.

- --skel | -s *(default: basic)* - The pre-made skeleton to use for the project. 
    - `basic` : Basic skeleton
    - `api` : A skeleton for RESTful API
    - `admin`: A skeleton for admin interface
    - `app`: A full fledge skeleton with login, blogs, etc.

Will create a `www` project with `basic` skeleton

    juice create --project www
    
Create a project name `api` with `api` skeleton

    juice create -p api --skel api

---

## serve

Allow to launch the project in local dev environment.

**Args**

- --project | -p: The name of the project

- --port *(default: 5000)* - The port to use if you want to use one other than 5000

This will launch the `www` project under port 5000

    juice serve -p www

This will launch the `api` project under port 5001

    juice serve -p api --port 5001

---

## buildassets

Allows to build web assets static files.

**Args**

- --project | -p : The name of the project

This will build your assets for the `www` project

    juice buildassets -p www

---

## assets2s3

If you want to host your assets on AWS S3, **juice** can conveniently upload 
them on S3.

**Args**

- --project | -p : The name of the project

The example below will build and upload to S3 your static files. 
It will be reflected autmatically in your code.

    juice assets2s3 -p www

By default the `Development` config will be used. 
If you want to use the `PRODUCTION` to upload from your local machine:

    ENV='PRODUCTION' juice assets2s3 -p www

---

## push

This is convenient command to push your application to production server by using GIT.

No need to add a remote manually. By specifying the remote in your `propel.yml`
file, it will push it to that remote. This will allow to quickly change the remotes
to push to. Of course you must commit your code.

**Args**

- --remote | -r : The remote to push to

- --all : To push to all remotes

In your `/propel.yml` file, edit the section `git-remotes`:


    git-remotes:
      web:
        - ssh://user@host/path.git
        - ssh://user@host2/application-name.git
      workers:
        - ssh://user@host3/another.git

Now to push to `web` only:

    juice push --remote web

To push `workers`:

    juice push -r workers
    
To push to all remotes:

    juice push --all




