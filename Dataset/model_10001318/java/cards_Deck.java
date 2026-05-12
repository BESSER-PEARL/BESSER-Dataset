





import java.util.List;
import java.util.ArrayList;

public class cards_Deck  {

    private String cards;
    private int remain;



    public cards_Deck(
        String cards,        int remain    ) {
        this.cards = cards;
        this.remain = remain;
    }


    public String getCards() {
        return cards;
    }

    public void setCards(String cards) {
        this.cards = cards;
    }
    public int getRemain() {
        return remain;
    }

    public void setRemain(int remain) {
        this.remain = remain;
    }


}