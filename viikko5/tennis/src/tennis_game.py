class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player):
        if player == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def equal_scores(self):
        if self.player1_score == 0:
            return "Love-All"
        elif self.player1_score == 1:
            return "Fifteen-All"
        elif self.player1_score == 2:
            return "Thirty-All"
        else:
            return"Deuce"
    
    def four_or_more_points(self):
        point_distance = self.player1_score - self.player2_score

        if point_distance == 1:
            return "Advantage player1"
        elif point_distance == -1:
            return "Advantage player2"
        elif point_distance >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
    
    def other_point_scenarios(self):
        score_counter = 0
        score = ""
        for i in range(2):
            if i == 0:
                score_counter = self.player1_score
            else:
                score = score + "-"
                score_counter = self.player2_score

            if score_counter == 0:
                score += "Love"
            elif score_counter == 1:
                score += "Fifteen"
            elif score_counter == 2:
                score += "Thirty"
            elif score_counter == 3:
                score += "Forty"

        return score
    
    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.equal_scores()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.four_or_more_points()
        
        return self.other_point_scenarios()
