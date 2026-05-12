





import java.util.List;
import java.util.ArrayList;

public class Al_player  {

    private int points;
    private int bet;



    public Al_player(
        int points,        int bet    ) {
        this.points = points;
        this.bet = bet;
    }


    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }
    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }


}