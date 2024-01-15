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

class Result(dict):
    """
    A dotdict that represents the response from the API.

    Args:
        dict (dict): The dictionary to convert to a dotdict.

    Returns:
        Result (dotdict): The dotdict representation of the dictionary.
    """

    def __init__(self, *args, **kwargs):
        super(Result, self).__init__(*args, **kwargs)
        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = Result(value)
            elif isinstance(value, list):
                self[key] = [Result(item) if isinstance(item, dict) else item for item in value]

    def __getattr__(self, attr):
        return self.get(attr, None)

    def __getitem__(self, key):
        return self.get(key, None)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        del self[key]

    def __setitem__(self, key, value):
        super(Result, self).__setitem__(key, value)

    def __delitem__(self, key):
        super(Result, self).__delitem__(key)
