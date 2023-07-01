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


class TimeoutError(Exception):
    """Incase request times out"""
    def __init__(self, error):
        self.error = error
        self.success = False
        self.message = "Internal Server Timeout, Please try again later"

    def __str__(self):
        return f"{self.message}"


class InvalidRequest(Exception):
    """Incase request params is invalid"""
    def __init__(self, error):
        self.error = error
        self.success = False
        self.message = "Invalid Request, Please read docs: https://api.safone.me/redoc"

    def __str__(self):
        return f"{self.message}"


class InvalidContent(Exception):
    """Incase returned content is invalid"""
    def __init__(self, error):
        self.error = error
        self.success = False
        self.message = "Invalid Content Received, Please report this: https://api.safone.me/report"

    def __str__(self):
        return f"{self.message}"


class GenericApiError(Exception):
    """Incase api returns validation error"""
    def __init__(self, error):
        self.error = error
        self.success = False
        self.message = "Generic Api Call Failed, Please report this: https://api.safone.me/report"

    def __str__(self):
        return f"{self.message}"


class ConnectionError(Exception):
    """Incase unable to connect with site"""
    def __init__(self, error):
        self.error = error
        self.success = False
        self.message = "Failed to communicate with api, Please report this: https://api.safone.me/report"

    def __str__(self):
        return f"{self.message}"
