"""
SafoneAPI v1.0
Copyright (c) 2023 AsmSafone

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
    message = "An error occurred"

    def __init__(self, error=None):
        self.success = False
        self.error_message = error or self.message

    def __str__(self):
        return self.message


class TimeoutError(BaseError):
    message = "Request Timeout, Please try again later"


class RateLimitExceeded(BaseError):
    message = "Rate Limit Exceeded, Please try again later"


class InvalidRequest(BaseError):
    message = "Invalid Request, Please read docs: https://api.safone.dev/redoc"


class InvalidContent(BaseError):
    message = "Invalid Content, Please report this: https://api.safone.dev/report"


class GenericApiError(BaseError):
    message = "Api Call Failed, Please report this: https://api.safone.dev/report"


class ConnectionError(BaseError):
    message = "Failed to communicate server, Please report this: https://api.safone.dev/report"
