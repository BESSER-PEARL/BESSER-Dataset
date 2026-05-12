





import java.util.List;
import java.util.ArrayList;

public class Cards_StarndardDeck  {

    private String rand;
    private None cards;





    private Cards_Card cards_card;


    public Cards_StarndardDeck(
        String rand,        None cards    ) {
        this.rand = rand;
        this.cards = cards;
    }


    public String getRand() {
        return rand;
    }

    public void setRand(String rand) {
        this.rand = rand;
    }
    public None getCards() {
        return cards;
    }

    public void setCards(None cards) {
        this.cards = cards;
    }

    public Cards_Card getCards_card() {
        return cards_card;
    }

    public void setCards_card(Cards_Card cards_card) {
        this.cards_card = cards_card;
    }

}