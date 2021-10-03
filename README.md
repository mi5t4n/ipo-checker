# IPO Checker
Checks more than one account for an IPO.

    Usage: ipo_checker.py [-h] --company COMPANY --file FILE

    IPO Checker for a list.

    optional arguments:
    -h, --help         show this help message and exit
    --company COMPANY  Company ID
    --file FILE        Name of the pattern file.


# Requirements
1. Python 3.6+

# Installation
1. Install [pipenv](https://pipenv.pypa.io/en/latest/).
2. Initialize virtualize environment in the project folder using `pipenv shell`.
3. Install python libraries `pipenv install`

# How to get company ID?
1. Open the [ipo result](https://iporesult.cdsc.com.np/) in the browser.
2. Open the developer tools or type `Ctrl+Shift+I`.
3. Get the company ID.
    
![2021-10-03_18-49](https://user-images.githubusercontent.com/8264719/135754876-96ae31ea-1b8a-4dbd-9d76-5b0163c2d057.png)


# How to use the tool?
    python ipo_checker.py --file=list.txt --company=18

    [John Doe] :: Congratulation Alloted !!! Alloted quantity : 10
    [Joshue Doe] :: Sorry, not alloted for the entered BOID.
