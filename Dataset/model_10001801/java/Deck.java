





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private int deck_position;
    private String deck_of_cards;





    private List<Card> cards;


    public Deck(
        int deck_position,        String deck_of_cards    ) {
        this.deck_position = deck_position;
        this.deck_of_cards = deck_of_cards;
        this.cards = new ArrayList<>();
    }

    public Deck(
        int deck_position,        String deck_of_cards        ArrayList<Card> cards    ) {
        this.deck_position = deck_position;
        this.deck_of_cards = deck_of_cards;
        this.cards = cards;
    }

    public int getDeck_position() {
        return deck_position;
    }

    public void setDeck_position(int deck_position) {
        this.deck_position = deck_position;
    }
    public String getDeck_of_cards() {
        return deck_of_cards;
    }

    public void setDeck_of_cards(String deck_of_cards) {
        this.deck_of_cards = deck_of_cards;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}