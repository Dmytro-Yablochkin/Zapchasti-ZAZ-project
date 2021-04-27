*** Settings ***
Documentation    Testing web-site functionality

Library    SeleniumLibrary
Library    page_objects/Registration.py
Library    page_objects/Authorization.py
Library    page_objects/OtherFunctionality.py
Library    page_objects/CartFunctionality.py
Library    page_objects/CompareFunctionality.py
Library    page_objects/OrderFunctionality.py
Library    page_objects/SearchFieldFunctionality.py
Library    page_objects/HeaderNavigation.py

Test Setup    OPEN BROWSER  ${MAIN_PAGE_URL}  chrome
Test Teardown    Close all browsers

*** Variables ***
${MAIN_PAGE_URL}    https://zapchastizaz.com.ua/
*** Test Cases ***

# REGISTRATION
1. Customer registration
    Create account
1.1 Negative creation an account
    Bad create account

# AUTHORIZATION
2. Authorization
    Redirect to auth form
    Input user email
    Input user password
    Submit authorization
    Check user is login

2.1 Authorisation with incorrect password
    Redirect to auth form
    Input user email
    Input incorrect password
    Submit authorization
    Check message alert

# OTHER FUNCRIONALITY
3. Add items modal window
    maximize browser window
    Click accessories btn
    Click iz04 item
    Add iz04 in cart
    Close modal window

# CART FUNCTIONALITY
4. Append/subtract item button
    maximize browser window
    Click markdown btn
    Click rsp96226990 item link
    Add current item to cart
    Click checkout btn
    Click append btn
    Check append is success
    Click subtract btn
    Check subtract is success

5. Removing an item from the cart
    maximize browser window
    Execute testcase id 4
    Click trash icon
    Check remove is success

# COMPARE FUNCTIONALITY
6. Compare adding items pop-up
    maximize browser window
    Hover takuma list item
    Click takuma chassis item
    Click 553339 item
    Click add to compare btn
    Check add to compare is success
    Close compare pop up
    Click add to compare btn
    Check delete from compare is success
    Close compare pop up

# CREATION ORDER FUNCTIONALITY
7. Check user can create an order
    maximize browser window
    User sign up
    Click accessories btn
    click 11022 3901094 item
    Add current item to cart
    Click checkout btn
    Check user info is correct
    Click continue btn
    Choose delivery method
    # Next step need user intervention

# compare functionality
8. Compare adding items pop-up closing
    maximize browser window
    Click lt 555 item
    Click add to compare btn
    Check add to compare is success
    Close compare pop up

# compare functionality
9. Compare different categories
    maximize browser window
    Hover takuma list item
    Click takuma chassis item
    Add to compare 553339 item
    Check add to compare is success
    Close compare pop up
    Add to compare PJC 051
    Check add to compare is success
    Close compare pop up
    Submit compare
    Check compare is success

# SARCH FIELD FUNCTIONALITY
10. Check check-box functionality
    maximize browser window
    Click search categories
    Click categories check boxes
    Submit search
    Check search result is success

# compare functionality
11. Compare items delete
    maximize browser window
    Execute testcase id 9
    Delete item from compare
    Check deleting is success

# oter functionality
12. Catalogue subcategories
    maximize browser window
    Hover takuma list item
    Click takuma chassis item
    Check redirect is success


# creation order functionality
13. Check not registered user can create an order via Nova Poshta
    maximize browser window
    Add item to cart
    Input user data in order form
    Submit user data
    Choose Nova Poshta delivery method
    Choose city to delivery
    Choose delivery warehouse
    # Next step need user intervention

# creation order functionality
14. Creating multi order via Justin
    maximize browser window
    Add items to cart
    Input user data in order form 2
    Submit user data
    Choose justin delivery
    Choose justin city address
    # Next step need user intervention

# cart functionality
15. Saving cart information functionality
    maximize browser window
    Check saving info is success

# other functionality
16. Check user can navigate to Contacts page
    maximize browser window
    Click header contacts
    Check contact page redirecting is success

# cart functionality
17. Delete item from cart droplist
    Add to cart
    Close modal window
    Delete from cart droplist
    Check deleting is successfull

# search field functionality
18. Check user can take search result using incorrect search data
    maximize browser window
    Input incorrect search data
    Submit search
    Check search result is success