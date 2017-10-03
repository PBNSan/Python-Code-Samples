# Quiz: Break the String
# Time to write your own loop with a break statement. Your task is to create a string, news_ticker that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

# Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs.

def newsticker_func():

      headlines = ["Local Bear Eaten by Man","Legi slature Announces New Laws","Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

      news_ticker = ""

# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs

      #Approach 1
#       diff = 0

#       for i in range(len(headlines)):
#             news_ticker +=  headlines[i] + " "
#            # diff = 140 - len(news_ticker)

#             if(len(news_ticker) + len(headlines[i+1]) > 140):
#             # slice the next list object and add it to the newsticker variable
#                   diff = 140 - len(news_ticker)
#                   news_ticker += " " + headlines[i][0:diff-1]
#                   break
#       print(len(news_ticker))
#       return print(news_ticker)

      #Approach 2
      for headline in headlines:
            news_ticker += headline + " "
            if len(news_ticker) >= 140:
                  news_ticker = news_ticker[:140]
                  break

      return print(news_ticker)

newsticker_func() 