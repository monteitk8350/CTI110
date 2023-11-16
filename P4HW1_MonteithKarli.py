 # CTI-110
 # P4HW1 - Score List
 # Karli Monteith
 # 11/15/2023
def main():
  """
  Main function to collect and process user scores.
  """
  num_scores = int(input("Enter the number of scores you would like to enter: "))
  scores = []

  #Generate scores
  for i in range(num_scores):
      valid_score = False
      while not valid_score:
          score = int(input(f"Enter score {i+1}: "))
          if 0 <= score <= 100:
              scores.append(score)
              valid_score = True
          else:
              print("Invalid score. Please enter a score between 0 and 100.")

  #Show low score
  print(f"Lowest score entered: {min(scores)}")

  #lowest score
  scores.remove(min(scores))

  #Calculate avg
  avg_score = sum(scores) / len(scores)
  print(f"Score List after dropping lowest score: {scores}")
  print(f"Average of scores in modified list: {avg_score}")

  #Find letter grade
  letter_grade = determine_letter_grade(avg_score)
  print(f"Letter grade for the calculated average: {letter_grade}")


def determine_letter_grade(avg_score):
  """
  Determine the letter grade based on the average score.

  Args:
  average_score (float): The average score

  Returns:
  str: The letter grade
  """
  if 90 <= avg_score <= 100:
      return "A"
  elif 80 <= avg_score < 90:
      return "B"
  elif 70 <= avg_score < 80:
      return "C"
  elif 60 <= avg_score < 70:
      return "D"
  else:
      return "F"


if __name__ == "__main__":
  main()