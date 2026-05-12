





import java.util.List;
import java.util.ArrayList;

public class CommunityCards  {

    private String cards;





    private Card card;


    public CommunityCards(
        String cards    ) {
        this.cards = cards;
    }


    public String getCards() {
        return cards;
    }

    public void setCards(String cards) {
        this.cards = cards;
    }

    public Card getCard() {
        return card;
    }

    public void setCard(Card card) {
        this.card = card;
    }

}