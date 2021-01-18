# WK1
In this week we'll be building out the foundation of your app, in particular, the UI aspect.
This will make use of your ability to print to the screen, clear the screen, accept user input, and create a basic `list` data structure.
Try to make good use of functions for repetitive tasks.
## Goals
As a user I want to:
- create a product and add it to a list
- view all products
- _STRETCH_ update or delete a product
## Spec
A `product` should just be a `string` containing its name, i.e: `"Coke Zero"`
A list of `products` should be a list of `strings`, i.e: `["Coke Zero"]`
## Pseudo Code
- START APP
- SHOW LIST OF OPTIONS TO USER AND ACCEPT NUMERICAL INPUT
- IF USER ENTERS `0` THEN EXIT APP
- IF USER ENTERS `1` THEN SHOW `PRODUCT` MENU
  - IF USER ENTERS `0` RETURN TO MAIN MENU
  - IF USER ENTERS `1` PRINT OUT `PRODUCTS` TO SCREEN
  - IF USER ENTER `2` CREATE NEW `PRODUCT`
    - ASK USER FOR THE `NAME` OF THE `PRODUCT`
    - APPEND THIS TO THE LIST OF `PRODUCTS`
  - _STRETCH_ IF USER ENTERS `3` UPDATE `PRODUCT`
    - ASK USER TO SELECT A `PRODUCT` TO UPDATE
    - ASK USER FOR NEW `NAME` OF `PRODUCT`
    - REPLACE `PRODUCT` AT SELECTED `IDX` WITH NEW `NAME`
  - _STRETCH_ IF USER ENTERS `4` DELETE `PRODUCT`
    - ASK USER TO SELECT A `PRODUCT` TO DELETE
    - REMOVE THIS ITEM FROM THE `PRODUCT` LIST