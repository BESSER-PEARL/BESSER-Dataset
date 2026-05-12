





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private None card;
    private String deck___;





    private Game game;




    private List<Card> cards;


    public Deck(
        None card,        String deck___    ) {
        this.card = card;
        this.deck___ = deck___;
        this.cards = new ArrayList<>();
    }

    public Deck(
        None card,        String deck___        ArrayList<Card> cards    ) {
        this.card = card;
        this.deck___ = deck___;
        this.cards = cards;
    }

    public None getCard() {
        return card;
    }

    public void setCard(None card) {
        this.card = card;
    }
    public String getDeck___() {
        return deck___;
    }

    public void setDeck___(String deck___) {
        this.deck___ = deck___;
    }

    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }
    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}