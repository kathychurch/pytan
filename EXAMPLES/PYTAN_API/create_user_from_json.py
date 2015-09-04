#!/usr/bin/env python
"""
Export a user object to a JSON file, adding ' API TEST' to the name of the user before exporting the JSON file and deleting any pre-existing user with the same (new) name, then create a new user object from the exported JSON file
"""
# import the basic python packages we need
import os
import sys
import tempfile
import pprint
import traceback

# disable python from generating a .pyc file
sys.dont_write_bytecode = True

# change me to the path of pytan if this script is not running from EXAMPLES/PYTAN_API
pytan_loc = "~/gh/pytan"
pytan_static_path = os.path.join(os.path.expanduser(pytan_loc), 'lib')

# Determine our script name, script dir
my_file = os.path.abspath(sys.argv[0])
my_dir = os.path.dirname(my_file)

# try to automatically determine the pytan lib directory by assuming it is in '../../lib/'
parent_dir = os.path.dirname(my_dir)
pytan_root_dir = os.path.dirname(parent_dir)
lib_dir = os.path.join(pytan_root_dir, 'lib')

# add pytan_loc and lib_dir to the PYTHONPATH variable
path_adds = [lib_dir, pytan_static_path]
[sys.path.append(aa) for aa in path_adds if aa not in sys.path]

# import pytan
import pytan

# create a dictionary of arguments for the pytan handler
handler_args = {}

# establish our connection info for the Tanium Server
handler_args['username'] = "Administrator"
handler_args['password'] = "Tanium2015!"
handler_args['host'] = "10.0.1.240"
handler_args['port'] = "443"  # optional

# optional, level 0 is no output except warnings/errors
# level 1 through 12 are more and more verbose
handler_args['loglevel'] = 1

# optional, use a debug format for the logging output (uses two lines per log entry)
handler_args['debugformat'] = False

# optional, this saves all response objects to handler.session.ALL_REQUESTS_RESPONSES
# very useful for capturing the full exchange of XML requests and responses
handler_args['record_all_requests'] = True

# instantiate a handler using all of the arguments in the handler_args dictionary
print "...CALLING: pytan.handler() with args: {}".format(handler_args)
handler = pytan.Handler(**handler_args)

# print out the handler string
print "...OUTPUT: handler string: {}".format(handler)

# setup the arguments for the handler.get() method
get_kwargs = {}
get_kwargs["objtype"] = u'user'
get_kwargs["id"] = 1

# get objects to use as an export to JSON file
print "...CALLING: handler.get() with args: {}".format(get_kwargs)
orig_objs = handler.get(**get_kwargs)

# set the attribute name and value we want to add to the original objects
# this is necessarry to avoid name conflicts when adding the new object
attr_name = u'name'
attr_value = u' API TEST'

# modify the orig_objs to add attr_value to attr_name
for x in orig_objs:
    new_attr = getattr(x, attr_name)
    new_attr += attr_value
    setattr(x, attr_name, new_attr)

    # delete the object in case it already exists
    del_kwargs = {}
    del_kwargs[attr_name] = new_attr
    del_kwargs['objtype'] = u'user'

    print "...CALLING: handler.delete() with args: {}".format(del_kwargs)
    try:
        handler.delete(**del_kwargs)
    except Exception as e:
        print "...EXCEPTION: {}".format(e)

# export orig_objs to a json file
export_kwargs = {}
export_kwargs['obj'] = orig_objs
export_kwargs['export_format'] = 'json'
export_kwargs['report_dir'] = tempfile.gettempdir()

print "...CALLING: handler.export_to_report_file() with args: {}".format(export_kwargs)
json_file, results = handler.export_to_report_file(**export_kwargs)

# create the object from the exported JSON file
create_kwargs = {}
create_kwargs['objtype'] = u'user'
create_kwargs['json_file'] = json_file

print "...CALLING: handler.create_from_json() with args {}".format(create_kwargs)
response = handler.create_from_json(**create_kwargs)

print "...OUTPUT: Type of response: ", type(response)

print "...OUTPUT: print of response:"
print response

# call the export_obj() method to convert response to JSON and store it in out
export_kwargs = {}
export_kwargs['obj'] = response
export_kwargs['export_format'] = 'json'

print "...CALLING: handler.export_obj() with args {}".format(export_kwargs)
out = handler.export_obj(**export_kwargs)

# trim the output if it is more than 15 lines long
if len(out.splitlines()) > 15:
    out = out.splitlines()[0:15]
    out.append('..trimmed for brevity..')
    out = '\n'.join(out)

print "...OUTPUT: print the objects returned in JSON format:"
print out

'''STDOUT from running this:
...CALLING: pytan.handler() with args: {'username': 'Administrator', 'record_all_requests': True, 'loglevel': 1, 'debugformat': False, 'host': '10.0.1.240', 'password': 'Tanium2015!', 'port': '443'}
...OUTPUT: handler string: PyTan v2.1.0 Handler for Session to 10.0.1.240:443, Authenticated: True, Platform Version: 6.5.314.4301
...CALLING: handler.get() with args: {'objtype': u'user', 'id': 1}
...CALLING: handler.delete() with args: {'objtype': u'user', u'name': u'Administrator API TEST'}
...CALLING: handler.export_to_report_file() with args: {'report_dir': '/var/folders/dk/vjr1r_c53yx6k6gzp2bbt_c40000gn/T', 'export_format': 'json', 'obj': <taniumpy.object_types.user_list.UserList object at 0x11a871710>}
...CALLING: handler.create_from_json() with args {'objtype': u'user', 'json_file': '/var/folders/dk/vjr1r_c53yx6k6gzp2bbt_c40000gn/T/UserList_2015_09_03-22_44_44-EDT.json'}
...OUTPUT: Type of response:  <class 'taniumpy.object_types.user_list.UserList'>
...OUTPUT: print of response:
UserList, len: 1
...CALLING: handler.export_obj() with args {'export_format': 'json', 'obj': <taniumpy.object_types.user_list.UserList object at 0x102009ed0>}
...OUTPUT: print the objects returned in JSON format:
{
  "_type": "users", 
  "user": [
    {
      "_type": "user", 
      "deleted_flag": 0, 
      "group_id": 0, 
      "id": 271, 
      "last_login": "2001-01-01T00:00:00", 
      "local_admin_flag": 1, 
      "name": "Administrator API TEST", 
      "permissions": {
        "_type": "permissions", 
        "permission": [
          "admin", 
..trimmed for brevity..

'''

'''STDERR from running this:

'''
