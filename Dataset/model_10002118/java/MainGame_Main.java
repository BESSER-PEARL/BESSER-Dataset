





import java.util.List;
import java.util.ArrayList;

public class MainGame_Main  {

    private int dealNumber;
    private None deck;



    public MainGame_Main(
        int dealNumber,        None deck    ) {
        this.dealNumber = dealNumber;
        this.deck = deck;
    }


    public int getDealnumber() {
        return dealNumber;
    }

    public void setDealnumber(int dealNumber) {
        this.dealNumber = dealNumber;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }


}