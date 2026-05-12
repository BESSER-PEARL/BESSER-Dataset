





import java.util.List;
import java.util.ArrayList;

public class Group  {

    private int ID;
    private String name;





    private List<Deck> decks;


    public Group(
        int ID,        String name    ) {
        this.ID = ID;
        this.name = name;
        this.decks = new ArrayList<>();
    }

    public Group(
        int ID,        String name        ArrayList<Deck> decks    ) {
        this.ID = ID;
        this.name = name;
        this.decks = decks;
    }

    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
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