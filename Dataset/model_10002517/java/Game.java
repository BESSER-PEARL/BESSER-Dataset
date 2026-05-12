





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private String name;





    private List<Deck> decks;


    public Game(
        String name    ) {
        this.name = name;
        this.decks = new ArrayList<>();
    }

    public Game(
        String name        ArrayList<Deck> decks    ) {
        this.name = name;
        this.decks = decks;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Deck> getDecks() {
        return decks;
    }

    public void addDeck(Deck deck) {
        this.decks.add(deck);
    }

}