from ungreat_matching import ungreat_match


test_data = [['python','Python'],['python','python3.7'],['PYTHON','python3.7']]
for data in test_data:
    print(ungreat_match(data[0],data[1]))