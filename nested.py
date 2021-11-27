### nesting if-else
### modeling : case step by step


is_the_phone_switched_on = True # bool
baterry_charge           = 20    # int % 

# A < B       A == B       A > B

if is_the_phone_switched_on ==True: # == True
    if baterry_charge >= 2:    
        print("FRIED CALLED!")


# dest: will this person call his friend ?





"""
     DIAGRAM/Path Search

     \*/  
      |
     / \
      x A
      | 
      |
      |
      |
      |
      x  if straigh go? --> (else)
      v True               v False    
      v                    v  
      v                    v 
      x if <obstacle yes>? v
      v  True      v False v 
      v            v       v
      v            v       v
      x <--------- v       v
      v                    v
      x <----------------- v
      |
      |
      |
      V B

"""
