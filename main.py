#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re
import cgi


page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a>Signup</a>
    </h1>
"""


page_footer = """
</body>
</html>
"""

user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and user_re.match(username)

pass_re = re.comnpile(r"^.{3,20}$")
def valid_password(password):
    return password and user_re.match(password)

email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return email and user_re.match(email)

class MainHandler(webapp2.RequestHandler):

    def get(self):
        signup_form = """
        <form action='/welcome' method='post'>
            <table>
                <tr>
                    <td><label for="username">Username: </label></td>
                    <td><input type="text" name="username"></td>
                </tr>
                <tr>
                    <td><label for="password">Password: </label></td>
                    <td><input type="password" name="password"></td>
                </tr>
                <tr>
                    <td><label for="verify_password">Verify Password: </label></td>
                    <td><input type="password" name="verify_password"></td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional): </label></td>
                    <td><input type="text" name="email"></td>
                </tr>
            </table>
            <input type="submit">
        </form>
        """

        content = page_header + signup_form + page_footer
        self.response.write(content)

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        if not_valid_username(username):
            user_error = "That's not a valid username."
            have_error = True

        if not_valid_password(password):
            pass_error = "That wasn't a valid password."
            have error = True
        elif password != verify_password:
            verify_error = "Your passwords didn't match."
            have_error = True

        if not_valid_email(email):
            email_error = "That's not a valid email."
            have_error = True

class welcome(webapp2.RequestHandler):
    def post(self):
        username = self.request.get('username')
        username_escaped = cgi.escaped(username)
        content = "<h2> Welcome, " + username + "!</h2>"


app = webapp2.WSGIApplication([
('/', MainHandler)
('/welcome, Welcome)
], debug=True)
