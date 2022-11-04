import main

def test_app_main_web_status():
    session = main.main()

    assert session == 200, "Server failed to connect to web app"