import webapp2
class mainPage(webapp2.RequestHandler):
    def get (self):
        self.response.write("Anuja Ayush Ajinkya")
app=webapp2.WSGIApplication([('/',mainPage)],debug=True)