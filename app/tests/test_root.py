def test_root(test_app):
    response = test_app.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Let it Snow! Let it Snow! Let it Snow!"}