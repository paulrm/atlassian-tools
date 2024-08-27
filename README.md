# atlassian-tools

to install requiered modules

`pip install python-dateutil humanize requests`


# Error
```
/Users/paul/src/atlassian-tools/issues.py:46: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.utcnow()
Traceback (most recent call last):
  File "/Users/paul/src/atlassian-tools/issues.py", line 67, in <module>
    main()
  File "/Users/paul/src/atlassian-tools/issues.py", line 63, in main
    elapsed_time = format_elapsed_time(updated_time_str)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/paul/src/atlassian-tools/issues.py", line 47, in format_elapsed_time
    elapsed_time = now - updated_time
                   ~~~~^~~~~~~~~~~~~~
TypeError: can't subtract offset-naive and offset-aware datetimes
```