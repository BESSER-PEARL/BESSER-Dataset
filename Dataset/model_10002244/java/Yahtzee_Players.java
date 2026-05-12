





import java.util.List;
import java.util.ArrayList;

public class Yahtzee_Players  {

    private String Score;
    private String Name;





    private Yahtzee_Scoring yahtzee_scoring;




    private Yahtzee_Turn yahtzee_turn;




    private Yahtzee_Game yahtzee_game;


    public Yahtzee_Players(
        String Score,        String Name    ) {
        this.Score = Score;
        this.Name = Name;
    }


    public String getScore() {
        return Score;
    }

    public void setScore(String Score) {
        this.Score = Score;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Yahtzee_Scoring getYahtzee_scoring() {
        return yahtzee_scoring;
    }

    public void setYahtzee_scoring(Yahtzee_Scoring yahtzee_scoring) {
        this.yahtzee_scoring = yahtzee_scoring;
    }
    public Yahtzee_Turn getYahtzee_turn() {
        return yahtzee_turn;
    }

    public void setYahtzee_turn(Yahtzee_Turn yahtzee_turn) {
        this.yahtzee_turn = yahtzee_turn;
    }
    public Yahtzee_Game getYahtzee_game() {
        return yahtzee_game;
    }

    public void setYahtzee_game(Yahtzee_Game yahtzee_game) {
        this.yahtzee_game = yahtzee_game;
    }

}