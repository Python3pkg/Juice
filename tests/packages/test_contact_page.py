
from webmaster import Webmaster
from webmaster.decorators import extends
from webmaster.packages import contact_page
from tests import config

def test_contact_page():

    @extends(contact_page.contact_page)
    class Index(Webmaster):
        pass

    app = Webmaster.init(__name__, config=config)
    app.testing = True

    with app.test_client() as c:
        data = c.get("/contact").data
