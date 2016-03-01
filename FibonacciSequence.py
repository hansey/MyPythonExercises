def fibonacci_sequence(
        var_item_number):
    var_leader_first=0
    var_leader_second=1
    var_result_first=0
    var_result_second=0
    var_result=0
    for i in range(0,var_item_number):
        if i==0:
            var_result=var_leader_first
            var_result_first=var_leader_first
            print var_result
        elif i==1:
            var_result=var_leader_second
            var_result_second=var_leader_second
            print var_result
        else:
            var_result=var_result_first+var_result_second
            var_result_first=var_result_second
            var_result_second=var_result
            print var_result

fibonacci_sequence(10)