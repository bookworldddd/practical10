def calculate_total(marks):
  return sum(marks)
def calculate_average(matks):
  return calculate_total(marks) / len(marks)
def get_result(marks):
  average = calculate_average(marks)
  if average >=40:
    return "PASS"
  else:
    return "FAIL"
    
