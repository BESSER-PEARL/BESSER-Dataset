





import java.util.List;
import java.util.ArrayList;

public class __abstract___BaseDeck  {






    private List<PlayCard> playcards;




    private PokerTable pokertable;


    public __abstract___BaseDeck(
    ) {
        this.playcards = new ArrayList<>();
    }

    public __abstract___BaseDeck(
        ArrayList<PlayCard> playcards    ) {
        this.playcards = playcards;
    }


    public List<PlayCard> getPlaycards() {
        return playcards;
    }

    public void addPlaycard(Playcard playcard) {
        this.playcards.add(playcard);
    }
    public PokerTable getPokertable() {
        return pokertable;
    }

    public void setPokertable(PokerTable pokertable) {
        this.pokertable = pokertable;
    }

}