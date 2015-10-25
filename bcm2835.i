 %include "stdint.i"
 %module bcm2835
 %{
 /* Includes the header in the wrapper code */
 #include "../src/bcm2835.h"
 %}
 
 /* Parse the header file to generate wrappers */
 %include "../src/bcm2835.h"
