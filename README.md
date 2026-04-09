## Note
purgetower might get sliced janky
some layers are missing in the resultpattern

## Userinputs
- 'Do you want some Data for insights about the Gradient?(bool): '                 
  *-> expects 1, true, True, y or yes to give user data insights*
- 'enter first color value (int): '                
  *-> expects integer selector of first color*
- 'enter second color value (int): '               
  *-> expects integer selector of second color*
- 'enter size/layers of gradient (int): '          
  *-> expects integer value for gradient size in layers*
- 'enter lower mixing bound, defaults to 0% (int): '                 
  *-> expects integer value as lower mixing bound of first color*
- 'enter upper mixing bound, defaults to 100% (int): '                 
  *-> expects integer value as upper mixing bound of first color*
- 'enter offset in layers from the bottom, defaults to 0 (int): ' 
  *-> expects integer to offset gradient from buildplate (layer 1)*
- 'enter gadient stepsize, defaults to 5% (int): '                 
  *-> expects integer value as stepsize. example: 5 for 5% mixing-stepsize*
