





import java.util.List;
import java.util.ArrayList;

public class Game2  {

    private String name;





    private List<Deck2> deck2s;


    public Game2(
        String name    ) {
        this.name = name;
        this.deck2s = new ArrayList<>();
    }

    public Game2(
        String name        ArrayList<Deck2> deck2s    ) {
        this.name = name;
        this.deck2s = deck2s;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Deck2> getDeck2s() {
        return deck2s;
    }

    public void addDeck2(Deck2 deck2) {
        this.deck2s.add(deck2);
    }

}