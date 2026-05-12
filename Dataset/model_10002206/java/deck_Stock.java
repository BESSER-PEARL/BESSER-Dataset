





import java.util.List;
import java.util.ArrayList;

public class deck_Stock  {

    private String stock;
    private int STARTING_INDEX;





    private deck_Deck deck_deck;


    public deck_Stock(
        String stock,        int STARTING_INDEX    ) {
        this.stock = stock;
        this.STARTING_INDEX = STARTING_INDEX;
    }


    public String getStock() {
        return stock;
    }

    public void setStock(String stock) {
        this.stock = stock;
    }
    public int getStarting_index() {
        return STARTING_INDEX;
    }

    public void setStarting_index(int STARTING_INDEX) {
        this.STARTING_INDEX = STARTING_INDEX;
    }

    public deck_Deck getDeck_deck() {
        return deck_deck;
    }

    public void setDeck_deck(deck_Deck deck_deck) {
        this.deck_deck = deck_deck;
    }

}