

def sort_by_credits(leaderboard):
    for i in range(len(leaderboard)):
        for j in range(i+1,len(leaderboard)):
            if int(leaderboard[j].split()[0])>int(leaderboard[i].split()[0]):
                temp = leaderboard[j]
                leaderboard[j] = leaderboard[i]
                leaderboard[i] = temp
    return leaderboard            

def create_text_leaderboard(leaderboard_in,id):
    leaderboard = sort_by_credits(leaderboard_in)
    
    text = "<b>LEADERBOARD</b>\n"
    pos = 1
    for player in leaderboard:
        data_player = player.split()
        if int(data_player[2]) == id:
            text+="➤"
        else:    
            text+="    "
        if pos == 1:
            text += "🥇"
        else:
            if pos == 2:
                text += "🥈"
            else:
                if pos == 3:
                    text += "🥉"
                else:
                    text += " ⦿"
        if int(data_player[2]) == id:
            text+="<b>["+str(pos)+"] </b>"
            text += "<b>"+data_player[0]+" credits </b> "
            text += "<b>@"+data_player[1]+"</b>\n"
        else:
            text+="["+str(pos)+"] "
            text += data_player[0]+" credits "
            text += "@"+data_player[1]+"\n"
        pos+=1    
    return text

        