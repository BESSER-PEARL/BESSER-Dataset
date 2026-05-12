





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String hand;
    private String name;





    private Card card;


    public Player(
        String hand,        String name    ) {
        this.hand = hand;
        this.name = name;
    }


    public String getHand() {
        return hand;
    }

    public void setHand(String hand) {
        this.hand = hand;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Card getCard() {
        return card;
    }

    public void setCard(Card card) {
        this.card = card;
    }

}