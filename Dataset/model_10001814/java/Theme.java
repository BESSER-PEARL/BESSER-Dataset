





import java.util.List;
import java.util.ArrayList;

public class Theme  {






    private List<Deck> decks;


    public Theme(
    ) {
        this.decks = new ArrayList<>();
    }

    public Theme(
        ArrayList<Deck> decks    ) {
        this.decks = decks;
    }


    public List<Deck> getDecks() {
        return decks;
    }

    public void addDeck(Deck deck) {
        this.decks.add(deck);
    }

}