import logging

from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware (BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)
        self.logger = logging.getLogger()

    async def dispatch (self, request, call_next):

        # Log the request
        self.logger.info("Request", extra={'type':'api-request', 'method':str(request.method).upper(), 'url':str(request.url)})

        # Next middleware
        response = await call_next(request)

        # Log the response
        self.logger.info("Response sent", extra={'type':'api-response', 'code':response.status_code})
            
        # Return response
        return response