import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('static/templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())
class NewPost(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('static/templates/new_post.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())
class ViewPost(webapp2.RequestHandler):
    def post(self):
        title_variable = self.request.get('title')
        content_variable = self.request.get('content')
        author_variable = self.request.get('author')
        view_dict = {
        'title_var': title_variable,
        'content_var': content_variable,
        'author_var': author_variable,
        }
        template = jinja_env.get_template('static/templates/view_post.html')
        self.response.write(template.render(view_dict))
        print("You've submitted a new post")
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/post', NewPost),
    ('/view', ViewPost),
], debug=True)
