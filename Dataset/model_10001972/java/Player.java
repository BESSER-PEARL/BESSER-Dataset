





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private int totalScore;
    private String name;
    private None games;



    public Player(
        int totalScore,        String name,        None games    ) {
        this.totalScore = totalScore;
        this.name = name;
        this.games = games;
    }


    public int getTotalscore() {
        return totalScore;
    }

    public void setTotalscore(int totalScore) {
        this.totalScore = totalScore;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getGames() {
        return games;
    }

    public void setGames(None games) {
        this.games = games;
    }


}