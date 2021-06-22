from collections import Counter
from itertools import combinations_with_replacement

def get_juices_by_calories(file_name):
    try:
        # Read data from file
        file_data = open(file_name,'r').read().split('\n')

        # Intialize index
        calorie_index= 1
        juice_index = 2
        calorie_intake_index = 3

        final_result = []

        for _ in range(0,int(file_data[0])):
            result = []
            # Get the data from file object to variables
            m,*cal = map(int,file_data[calorie_index].split(" "))
            calories = cal[:m]
            list_of_fruit_juices = list(file_data[juice_index])
            calorie_intake = int(file_data[calorie_intake_index])

            # Count Juice stock
            juice_count = Counter(list_of_fruit_juices)
            
            # Sort the Juices by name and uniqueness
            unique_juice = sorted(list(juice_count))[:m]
            juice_calorie = {}
            
            # Create a Juice to Calorie mapping
            for i in range(0,m):
                juice_calorie[calories[i]]=unique_juice[i]

            # Check every combination of calorie intake and juice calories
            for i in range(1,len(unique_juice)+1):
                for combination in combinations_with_replacement(calories, i):
                    if sum(combination) == calorie_intake:
                        combination = list(combination)
                        result.append([juice_calorie.get(n,n) for n in combination])
            
            # Generate Result
            for data in result:
                flag = 1
                count = Counter(data)
                for juice in unique_juice:
                    if(count[juice]>juice_count[juice]):
                        flag = 0
                        break;
                if flag == 0:
                    final_result.append("SORRY, YOU JUST HAVE WATER")
                    break
                else:
                    final_result.append(''.join(data))
                    break;
            
            # Update the Indexes
            calorie_index=calorie_index + 3
            juice_index = juice_index + 3
            calorie_intake_index = calorie_intake_index + 3

        # Write the data to File
        fp = open("sample_output.txt","w")
        for data in final_result:    
            fp.writelines(data+"\n")
        fp.close()
    except Exception as ex:
        fp = open("error_log.txt","a")
        fp.write(str(ex))
        fp.close()
        
if __name__ == "__main__":
    file_name = input("Please enter input file name: ")
    get_juices_by_calories(file_name)
