#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Budget App (Simple CLI Version)

income_list = []
expense_list = []

def add_income(amount, source):
    income_list.append({
        "amount": amount,
        "source": source
    })
    print(f"✅ Income added: ₹{amount} from {source}")

def add_expense(amount, category, note=""):
    expense_list.append({
        "amount": amount,
        "category": category,
        "note": note
    })
    print(f"❌ Expense added: ₹{amount} for {category}")

def total_income():
    return sum(item["amount"] for item in income_list)

def total_expense():
    return sum(item["amount"] for item in expense_list)

def balance():
    return total_income() - total_expense()

def expense_summary():
    summary = {}
    for item in expense_list:
        category = item["category"]
        summary[category] = summary.get(category, 0) + item["amount"]
    
    print("\n📊 Expense Summary:")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")

def show_dashboard():
    print("\n💰 BUDGET DASHBOARD")
    print("-" * 30)
    print(f"Total Income : ₹{total_income()}")
    print(f"Total Expense: ₹{total_expense()}")
    print(f"Balance      : ₹{balance()}")
    expense_summary()


# In[2]:


add_income(30000, "Salary")
add_income(2000, "Freelance")


# In[3]:


add_expense(5000, "Rent")
add_expense(3000, "Food")
add_expense(1500, "Transport")


# In[4]:


show_dashboard()


# In[ ]:





# In[ ]:





# In[7]:



# DYNAMIC BUDGET APP 


class BudgetApp:
    """
    BudgetApp manages income, expenses, and balance.
    Designed to be simple, extensible, and beginner-friendly.
    """
class BudgetApp:
    def __init__(self, currency="₹"):
        # Currency symbol is configurable (₹, $, € etc.)
        self.currency = currency
        
        # List to store income entries
        # Each entry will be a dictionary
        self.incomes = []
        
        # List to store expense entries
        self.expenses = []

    # --------------------------------------
    # ADD INCOME
    # --------------------------------------
    def add_income(self, amount, source):
        """
        Adds an income record.
        amount: numeric value
        source: description of income (salary, freelance, etc.)
        """
        self.incomes.append({
            "amount": amount,
            "source": source
        })

 
    # ADD EXPENSE
  
    def add_expense(self, amount, category, note=None):
        """
        Adds an expense record.
        note is optional and helps in detailed tracking.
        """
        self.expenses.append({
            "amount": amount,
            "category": category,
            "note": note
        })


    def total_income(self):
        # Sum of all income amounts
        return sum(item["amount"] for item in self.incomes)

    def total_expense(self):
        # Sum of all expense amounts
        return sum(item["amount"] for item in self.expenses)

    def balance(self):
        # Balance is derived, not stored
        return self.total_income() - self.total_expense()


    def expense_by_category(self):
        """
        Returns expense totals grouped by category.
        """
        summary = {}
        for item in self.expenses:
            category = item["category"]
            summary[category] = summary.get(category, 0) + item["amount"]
        return summary


    def show_dashboard(self):
        """
        Displays the budget summary in a readable format.
        """
        print("\n💰 BUDGET DASHBOARD")
        print("-" * 35)

        print(f"Total Income : {self.currency}{self.total_income()}")
        print(f"Total Expense: {self.currency}{self.total_expense()}")
        print(f"Balance      : {self.currency}{self.balance()}")

        print("\n📊 Expense Breakdown:")
        for category, amount in self.expense_by_category().items():
            print(f"{category:<15} {self.currency}{amount}")


# In[8]:


# Create app instance
app = BudgetApp(currency="₹")

# Add income
app.add_income(30000, "Salary")
app.add_income(5000, "Freelance")

# Add expenses
app.add_expense(8000, "Rent")
app.add_expense(2500, "Food")
app.add_expense(1200, "Transport")

# View dashboard
app.show_dashboard()


# In[ ]:




