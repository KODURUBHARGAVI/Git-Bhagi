def filter_avg(data: list) -> dict:
    names=[name_score[0] for name_score in data if any(score>=75 for score in name_score[1])]
    scores=[name_score[1] for name_score in data if any(score>=75 for score in name_score[1])]
    scores1=[[seven_five for seven_five in ind_scores if seven_five>=75] for ind_scores in scores]
    avgs=[sum(scores)/len(scores) for scores in scores1]
    op_dict={}
    output={names[i]:avgs[i] for i in range(len(names))}
    return output
