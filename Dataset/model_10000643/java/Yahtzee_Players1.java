





import java.util.List;
import java.util.ArrayList;

public class Yahtzee_Players1  {

    private String compScore;
    private String playerScore;





    private Yahtzee_Display1 yahtzee_display1;


    public Yahtzee_Players1(
        String compScore,        String playerScore    ) {
        this.compScore = compScore;
        this.playerScore = playerScore;
    }


    public String getCompscore() {
        return compScore;
    }

    public void setCompscore(String compScore) {
        this.compScore = compScore;
    }
    public String getPlayerscore() {
        return playerScore;
    }

    public void setPlayerscore(String playerScore) {
        this.playerScore = playerScore;
    }

    public Yahtzee_Display1 getYahtzee_display1() {
        return yahtzee_display1;
    }

    public void setYahtzee_display1(Yahtzee_Display1 yahtzee_display1) {
        this.yahtzee_display1 = yahtzee_display1;
    }

}