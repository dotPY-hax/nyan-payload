# nyan-payload
nyan cat as a payload

This is a small Python project providing a simple Nyan Cat html page as a payload string. 
The payload holds the files from [nyan-cat-code](https://github.com/pyrat3/nyan-payload/tree/master/nyan-cat-code "nyan-cat-code") and copys them to the current directory with the [stager.py](https://github.com/pyrat3/nyan-payload/blob/master/stager.py "stager.py").
This is for educational use only.

Payloads are:

 -  [python_nyan_cat_payload.txt](https://github.com/pyrat3/nyan-payload/blob/master/python_nyan_cat_payload.txt "python_nyan_cat_payload.txt")
	 - ready to copy&paste into your (or someone elses) console /var/www/html *cough*
 - [python_nyan_cat_payload_with_exec_wrapper.txt](https://github.com/pyrat3/nyan-payload/blob/master/python_nyan_cat_payload_with_exec_wrapper.txt "python_nyan_cat_payload_with_exec_wrapper.txt")
	- ready to copy&paste into a Python interpreter
- [python_nyan_cat_payload_only.txt](https://github.com/pyrat3/nyan-payload/blob/master/python_nyan_cat_payload_only.txt "python_nyan_cat_payload_only.txt")
	- base64 with only the stager and the files ready for use in your own programs.

I also added the program I wrote for packing the files and stager together and creating the payload: [payloader.py](https://github.com/pyrat3/nyan-payload/blob/master/payloader.py "payloader.py")

**Things I might or might not do:**

  - Add more languages like php, bash, perl, go, whatever
  - an actual proper implementation of the nyan cat in js and/or html5
  - shrink down the size of the payload
  - cut the audio to a proper length so it is at least useable
  - look into optimizing the stager by using bytecode instead of proper Python syntax
  - look up if stager is actually the correct term to use...
  

KEEP NYANING

![KEEP NYANING](https://github.com/pyrat3/nyan-payload/blob/master/nyan-cat-code/nyan.gif)
