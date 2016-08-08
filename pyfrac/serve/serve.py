#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Mohit Sharma
# Aug 08 2016
# NYU CUSP 2016

"""
Module to Upload file to the server
"""

import pycurl
import os
import cStringIO
from pyfrac.utils import pyfraclogger

logger = pyfraclogger.pyfraclogger(tofile=True)
curl = pycurl.Curl()
response = cStringIO.StringIO()

URL = "uowebsite.cloudapp.net"
ID = "5 MTC"


def uploadFile(filename):
    """
    Upload file to `URL`
    Parameters
    ----------
    filename: str
        filename (with path) to be uploaded

    Returns
    -------
    response: cStringIO
        response returned by the server.
        Use `.getvalue() to parse the response
        to string`
    """
    curl.setopt(curl.POST, 1)
    curl.setopt(curl.URL, URL)
    curl.setopt(curl.HTTPHEADER, ['id: ' + ID])
    curl.setopt(curl.HTTPPOST, [('file1',
                                 (curl.FORM_FILE,
                                  os.path.abspath(filename))
                                 )])
    curl.setopt(curl.WRITEFUNCTION, response.write)
    curl.perform()
    curl.close()
    return response
