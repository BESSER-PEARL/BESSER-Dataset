





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private None cards;





    private BlackjackGame blackjackgame;




    private List<Card> cards;


    public Deck(
        None cards    ) {
        this.cards = cards;
        this.cards = new ArrayList<>();
    }

    public Deck(
        None cards        ArrayList<Card> cards    ) {
        this.cards = cards;
        this.cards = cards;
    }

    public None getCards() {
        return cards;
    }

    public void setCards(None cards) {
        this.cards = cards;
    }

    public BlackjackGame getBlackjackgame() {
        return blackjackgame;
    }

    public void setBlackjackgame(BlackjackGame blackjackgame) {
        this.blackjackgame = blackjackgame;
    }
    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}