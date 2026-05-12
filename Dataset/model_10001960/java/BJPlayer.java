





import java.util.List;
import java.util.ArrayList;

public class BJPlayer  {

    private String hands;
    private int bet;



    public BJPlayer(
        String hands,        int bet    ) {
        this.hands = hands;
        this.bet = bet;
    }


    public String getHands() {
        return hands;
    }

    public void setHands(String hands) {
        this.hands = hands;
    }
    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }


}