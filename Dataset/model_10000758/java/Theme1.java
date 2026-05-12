





import java.util.List;
import java.util.ArrayList;

public class Theme1  {

    private String name;
    private int year;





    private Game game;




    private List<Deck> decks;


    public Theme1(
        String name,        int year    ) {
        this.name = name;
        this.year = year;
        this.decks = new ArrayList<>();
    }

    public Theme1(
        String name,        int year        ArrayList<Deck> decks    ) {
        this.name = name;
        this.year = year;
        this.decks = decks;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }
    public List<Deck> getDecks() {
        return decks;
    }

    public void addDeck(Deck deck) {
        this.decks.add(deck);
    }

}