





import java.util.List;
import java.util.ArrayList;

public class Hand  {

    private int total;
    private None cards;



    public Hand(
        int total,        None cards    ) {
        this.total = total;
        this.cards = cards;
    }


    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }
    public None getCards() {
        return cards;
    }

    public void setCards(None cards) {
        this.cards = cards;
    }


}