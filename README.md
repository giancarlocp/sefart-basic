# Sefart-basic

To get more info visit [sefart.net](https://sefart.net/metodologia/)

This is the simplest code in this matter to save the initial effort.
The code is in Python with some functional programing style.
To start working with the encripted code in the torah, we need trhee(3) thing:

- **Genesis.txt:** a book to work with.
  We can find in [tanach.us](https://tanach.us/Server.txt?Genesis*&content=Consonants)

- **mispar.py:** a conversion table.
  We will work with the 22 letters Mispar-Hechrachi values.
  The are varians such as the Mispar-Gadol values, among others[1].

- **gematria.py:** the processor script.

To use the code:
- First download both *.py*
- Second download a book from the url suggested above.
- Move all of them to the same folder.
- Into the folder execute:
  `python3 gematria.py Genesis.txt`

You can check your results with:

![gematrix.org](https://raw.githubusercontent.com/giancarlocp/sefart-basic/master/img/gematrix.org.png)

The first lines result processing Genesis.txt is:

![result](https://raw.githubusercontent.com/giancarlocp/sefart-basic/master/img/result-example.png)

To get the mirror binary code we suggest insert the following lines after
we get `gem` in [gematria.py](https://github.com/giancarlocp/sefart-basic/blob/master/gematria.py#L23):
```python
binary = format(gem,'012b')
mirror = binary[::-1]
```

We don't save the processed info in any format.
The intention is give a basic code/knowlegde to start to work with.

Enjoy!

[1] https://en.wikipedia.org/wiki/Gematria
