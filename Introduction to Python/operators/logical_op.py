# checking eligibility of a client to apply for loan
has_high_income = True
has_good_credit = True
has_criminal_record = False

# AND operator
if has_high_income and has_good_credit:
    print("Eligible for loan")

# OR operator
if has_high_income or has_good_credit:
    print("Eligible for loan")


if has_high_income and not has_criminal_record:
    print("Eligible for loan")