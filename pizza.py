#!/usr/bin/env python
# coding: utf-8

# In[1]:


def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


# In[ ]:




