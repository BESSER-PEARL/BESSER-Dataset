





import java.util.List;
import java.util.ArrayList;

public class Players_Player  {

    private None hand;
    private String name;
    private int bet;



    public Players_Player(
        None hand,        String name,        int bet    ) {
        this.hand = hand;
        this.name = name;
        this.bet = bet;
    }


    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }


}