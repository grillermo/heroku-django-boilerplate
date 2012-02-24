class Generic(object):
    def process_request(self, request):
        '''
        Request: is an HttpRequest object. This method is called on each 
        request, before Django decides which view to execute
        process_request() should return either None or an HttpResponse object. 
        
        If it returns None, Django will continue processing this request, 
        executing any other middleware and, then, the appropriate view. If it 
        returns an HttpResponse object, Django won't bother calling ANY other 
        request, view or exception middleware, or the appropriate view; it'll
         return that HttpResponse. Response middleware is always called on 
         every response.
         '''
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        '''
        request is an HttpRequest object. view_func is the Python function 
        that Django is about to use. (It's the actual function object, not the 
        name of the function as a string.) view_args is a list of positional
        arguments that will be passed to the view, and view_kwargs is a 
        dictionary of keyword arguments that will be passed to the view.
        Neither view_args nor view_kwargs include the first view argument
        (request).
        
        process_view() is called just before Django calls the view. It should
        return either None or an HttpResponse object. If it returns None, 
        Django will continue processing this request, executing any other 
        process_view() middleware and, then, the appropriate view. If it 
        returns an HttpResponse object, Django won't bother calling ANY other
        request, view or exception middleware, or the appropriate view;
        it'll return that HttpResponse. Response middleware is always
        called on every response.
        '''
        context = {}
        return view_func(request,context=context,*view_args,**view_kwargs) 

    # def process_template_response(self, request, response):
    #     '''
    #     request is an HttpRequest object. response is a subclass of
    #     SimpleTemplateResponse (e.g. TemplateResponse) or any response object that
    #     implements a render method.

    #     process_template_response() must return a response object that implements a
    #     render method. It could alter the given response by changing
    #     response.template_name and response.context_data, or it could create and return
    #     a brand-new SimpleTemplateResponse or equivalent.

    #     process_template_response() will only be called if the response instance has a
    #     render() method, indicating that it is a TemplateResponse or equivalent.

    #     You don't need to explicitly render responses -- responses will be
    #     automatically rendered once all template response middleware has been called.

    #     Middleware are run in reverse order during the response phase, which includes
    #     process_template_response.
    #     '''
    #     return request, response

    # def process_response(self, request, response):
    #     '''
    #     request is an HttpRequest object. response is the HttpResponse object returned
    #     by a Django view.

    #     process_response() must return an HttpResponse object. It could alter the given
    #     response, or it could create and return a brand-new HttpResponse.

    #     Unlike the process_request() and process_view() methods, the process_response()
    #     method is always called, even if the process_request() and process_view()
    #     methods of the same middleware class were skipped because an earlier middleware
    #     method returned an HttpResponse (this means that your process_response() method
    #     cannot rely on setup done in process_request(), for example). In addition,
    #     during the response phase the classes are applied in reverse order, from the
    #     bottom up. This means classes defined at the end of MIDDLEWARE_CLASSES will be
    #     run first.
    #     '''
    #     return request, response
