---
layout: post
title:  "First Tech Post"
date:   2024-06-20 21:57:41 -0400
categories: python
---
Sample placeholder for tech posts

## Python
> Here's some python I wrote. Put this in a file named `filename.py` and run it with `python3 ./filename.py`

#### Code
``` python
def greet():
  """This function greets the user."""
  print("Hello, welcome!")

# Call the greet function
greet()
```

Or, if you don't like python, you can run some `powershell`
```powershell
# Get the list of running processes
$processes = Get-Process

# Save the list to a text file
$processes | Out-File -FilePath "C:\Temp\RunningProcesses.txt"
```

And finally `bash`

``` shell
#!/bin/bash

# Get the list of running processes
ps aux > /tmp/running_processes.txt
```