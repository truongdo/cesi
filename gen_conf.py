#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 truong-d <truong-d@truongd-ThinkPad-X1-Carbon-3rd>
#
# Distributed under terms of the MIT license.

"""

"""
import sys

hosts = sys.argv[1:]

for h in hosts:
    name, addr, username, password = h.split(",")
    print "[node:%s]" % (name)
    print "username = %s" % (username)
    print "password = %s" % (password)
    hostname, port = addr.split(":")
    print "host = %s" % (hostname)
    print "port = %s" % (port)
    print ""
