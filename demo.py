import web
import hashlib
import user

# Go to http://localhost:5984/_utils to create the databases.
# Change the names as needed.
user_dbname = 'demo_user'

urls = (
  '/(.*)/', 'Redirect',
  '/new', 'NewInstance',
  '/admin', 'Admin',
  '/', 'NewInstance'
)

app = web.application(urls, globals())

render = web.template.render('static')

class Admin:
    def GET(self):
        return "administration page"

class NewInstance:
    def GET(self):
        return render.superuser()
    def POST(self):
        input = web.input()
        user.create(user_dbname, 'root', \
          hashlib.sha256(input.password1).hexdigest(), type='superuser')
        raise web.seeother('/')

class Redirect:
    def GET(self, path):
        web.seeother('/' + path) 

class Login:
    def GET(self):
        return render.login()

if __name__ == '__main__':
    app.run()
