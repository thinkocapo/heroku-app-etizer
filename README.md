# heroku-app-etizer

### LOG


What I did / Questions
1. downloaded heroku cli
2. linked my herokucli to existing heroku apps
3. set Remote Heroku App but didn't deploy (use personal heroku for that)
4. Found sentry-demos-flask and Scheduler which has `generate_events.sh`
5. Learned must `git push heroku master` from master branch, which has `generate_events.sh`  
6. Learned - Set the frequency to be hourly. If the frequency is any higher, we would have to pay for the Dyno. Correct dyno stays running for 15minutes, then shuts down

### TODO

+create personal heroku account

- procfile for thinkocapo/flask, it [https://devcenter.heroku.com/articles/procfile](https://devcenter.heroku.com/articles/procfile)

- creat heroku flask app 

- Q. Must create Heroku App via GUI first? notion 'Deploy Backend Apps to Heroku' assumes this was already done?

- connect from React

- deploy willcapo.com, link custom domain name


### Questions
- Asked, could clone the heroku app, so you have copy of the original, then would have to paste your local branch's changes into it? (see will's screenshot)?
- Interesting Set the frequency to be hourly. If the frequency is any higher, we would have to pay for the Dyno?

## Heroku Setup

### Credentials

[https://id.heroku.com/login](https://id.heroku.com/login)
[Solutionsengineers@sentry.io](mailto:Solutionsengineers@sentry.io) password is in Password1

### Successful login brings you to

[https://dashboard.heroku.com/apps](https://dashboard.heroku.com/apps)

### Install cli

    npm install -g heroku
    heroku --version
    > heroku/7.29.0 darwin-x64 node-v12.3.0

- The CLI saves your email address and an API token to ~/.netrc for future use.
  ```
  cat ~/.netrc
  machine api.heroku.com
    login solutionsengineers@sentry.io
    password ******
  machine git.heroku.com
    login solutionsengineers@sentry.io
    password ******
  ```

### Heroku URL

[dashboard.heroku.com/apps](http://dashboard.heroku.com/apps) > select app > Settings > Info.Heroku Git Url


### How to Create New Heroku App

[The Procfile](https://devcenter.heroku.com/articles/procfile#procfile-format)

```
// heroku create <app_name>
flask git:(master) heroku create will-flask-demo
Creating ⬢ will-flask-demo... ⣾
Creating ⬢ will-flask-demo... done
https://will-flask-demo.herokuapp.com/ | https://git.heroku.com/will-flask-demo.git
```

vs

### How to Set Remote Heroku App

[https://devcenter.heroku.com/articles/git#for-an-existing-heroku-app](https://devcenter.heroku.com/articles/git#for-an-existing-heroku-app)

    ➜ express git:(master) ✗ heroku git:remote -a sentry-demos-express
    set git remote heroku to [https://git.heroku.com/sentry-demos-express.git](https://git.heroku.com/sentry-demos-express.git)

### How to Deploy (after Create or Set Remote)

`git push heroku master`

so instead of `origin master` ^ its a `origin master` ;)

### How to Scheduler

1. click sentry-demos-$APP
2. click Scheduler (plugin)
3. see it references `bash ./generate_events.sh`


## Other Commands

`heroku login`

or

`heroku login -i` for interactive mode, stay in CLI

Get recent logs:

`heroku logs --app sentry-demos-flask`

## Documentation & Commands

[Heroku Docs - The Process Model](https://devcenter.heroku.com/articles/process-model)

[Heroku Custom Domains - devcenter.heroku.com/articles/customer-domains](https://devcenter.heroku.com/articles/custom-domains)

[Heroku Procfile - The Process File](https://devcenter.heroku.com/articles/procfile)
