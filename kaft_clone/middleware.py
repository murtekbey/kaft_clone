def session_check_middleware(get_response):
    def middleware(request):
        if not request.session.session_key:
            request.session.save()
        response = get_response(request)
        print(request.session.session_key)

        return response

    return middleware
