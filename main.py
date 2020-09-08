# Author: Saeed Alshebli saa6016@psu.edu
# Collaborator: Caroline Brustoloni cxb5766@psu.edu
# Collaborator: Siddhant Rajoriya sbr5632@psu.edu
# Collaborator: John Sweetall jts6052@psu.edu
# Section: 2
# Breakout: 11

def getLetterGrade(grad):
  if grad >= 93.0:
    return 'A'
  elif grad >= 90.0:
    return 'A-'
  elif grad >= 87.0:
    return 'B+'
  elif grad >= 83.0:
    return 'B'
  elif grad >= 80.0:
    return 'B-'
  elif grad >= 77.0:
    return 'C+'
  elif grad >= 70.0:
    return 'C'
  elif grad >= 60.0:
    return 'D'
  elif grad < 60.0:
    return 'F'
def run():
  grad = float(input("Enter your CMPSC 131 garde: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(grad)}.")
if __name__== '__main__':
  run ()
