def MaximumDictionary(test_dict):
      result = {key:test_dict[key] for key in max(test_dict.keys())}
      return result

test_dict = {'1': 100, '2':200, '3':300}
print("Maximum of the dictionary :", MaximumDictionary)
