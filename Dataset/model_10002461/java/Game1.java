





import java.util.List;
import java.util.ArrayList;

public class Game1  {

    private String name;





    private List<Deck1> deck1s;


    public Game1(
        String name    ) {
        this.name = name;
        this.deck1s = new ArrayList<>();
    }

    public Game1(
        String name        ArrayList<Deck1> deck1s    ) {
        this.name = name;
        this.deck1s = deck1s;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Deck1> getDeck1s() {
        return deck1s;
    }

    public void addDeck1(Deck1 deck1) {
        this.deck1s.add(deck1);
    }

}