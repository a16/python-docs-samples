# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test script for Identity-Aware Proxy code samples."""

import make_iap_request
import validate_jwt

# The hostname of an application protected by Identity-Aware Proxy.
# When a request is made to https://${JWT_REFLECT_HOSTNAME}/, the
# application should respond with the value of the
# X-Goog-Authenticated-User-JWT (and nothing else.) The
# app_engine_app/ subdirectory contains an App Engine standard
# environment app that does this.
# The project must have the service account used by this test added as a
# member of the project.
REFLECT_SERVICE_HOSTNAME = '#######domain##########'
IAP_CLIENT_ID = '##################'

if __name__ == '__main__':
    # JWTs are obtained by IAP-protected applications whenever an
    # end-user makes a request.  We've set up an app that echoes back
    # the JWT in order to expose it to this test.  Thus, this test
    # exercises both make_iap_request and validate_jwt.
    iap_jwt = make_iap_request.make_iap_request(
        'https://{}/'.format(REFLECT_SERVICE_HOSTNAME), IAP_CLIENT_ID)
