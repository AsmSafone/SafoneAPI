"""
SafoneAPI v1.0
Copyright (c) 2024 AsmSafone

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class BaseError(Exception):
    """
    Base class for all exceptions raised by this library.

    Attributes:
        message (str): The error message.
        error_message (str): The error message.
        success (bool): The success status of the request.
    """
    message = "An error occurred!"

    def __init__(self, error=None):
        self.success = False
        self.error_message = error or self.message

    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return f"<{self.__class__.__name__} error_message='{self.error_message}'>"


class TimeoutError(BaseError):
    """
    Raised when a request times out.
    """
    message = "Request Timeout, Please try again later"


class RateLimitExceeded(BaseError):
    """
    Raised when the rate limit is exceeded.
    """
    message = "Rate Limit Exceeded, Please try again later"


class InvalidRequest(BaseError):
    """
    Raised when an invalid request is made.
    """
    message = "Invalid Request, Please read docs: https://api.safone.dev/redoc"


class InvalidContent(BaseError):
    """
    Raised when the content of the response is invalid.
    """
    message = "Invalid Content, Please report this: https://api.safone.dev/report"


class GenericApiError(BaseError):
    """
    Raised when the API returns an error that is not handled by this library.
    """
    message = "Api Call Failed, Please report this: https://api.safone.dev/report"


class ConnectionError(BaseError):
    """
    Raised when a connection error occurs.
    """
    message = "Failed to communicate server, Please report this: https://api.safone.dev/report"
