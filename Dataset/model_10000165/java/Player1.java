





import java.util.List;
import java.util.ArrayList;

public class Player1  {

    private String id;
    private int bet;
    private int points;



    public Player1(
        String id,        int bet,        int points    ) {
        this.id = id;
        this.bet = bet;
        this.points = points;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }
    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }


}