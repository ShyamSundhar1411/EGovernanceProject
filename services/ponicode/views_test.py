from services import views

class Test_Views_Preview_application:
    def test_preview_application_1(self):
        views.preview_application("GET", "Edmond", "consequatur-necessitatibus-sit")

    def test_preview_application_2(self):
        views.preview_application("DELETE", "Pierre Edouard", "quam-dignissimos-nostrum")

    def test_preview_application_3(self):
        views.preview_application("DELETE", "Pierre Edouard", "mollitia-quis-alias")

    def test_preview_application_4(self):
        views.preview_application("DELETE", "Jean-Philippe", "consequatur-necessitatibus-sit")

    def test_preview_application_5(self):
        views.preview_application("PUT", "Pierre Edouard", "est-dignissimos-earum")

    def test_preview_application_6(self):
        views.preview_application("", "", "")

    def test_preview_application_7(self):
        views.preview_application("GET", "Jean-Philippe", "est-dignissimos-earum")
