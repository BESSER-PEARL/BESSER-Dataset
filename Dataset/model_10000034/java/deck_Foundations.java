





import java.util.List;
import java.util.ArrayList;

public class deck_Foundations  {

    private String foundationList;





    private deck_Deck deck_deck;


    public deck_Foundations(
        String foundationList    ) {
        this.foundationList = foundationList;
    }


    public String getFoundationlist() {
        return foundationList;
    }

    public void setFoundationlist(String foundationList) {
        this.foundationList = foundationList;
    }

    public deck_Deck getDeck_deck() {
        return deck_deck;
    }

    public void setDeck_deck(deck_Deck deck_deck) {
        this.deck_deck = deck_deck;
    }

}