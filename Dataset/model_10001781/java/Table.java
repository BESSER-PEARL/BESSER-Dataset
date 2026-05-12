





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private String currPlayers;
    private None deck;



    public Table(
        String currPlayers,        None deck    ) {
        this.currPlayers = currPlayers;
        this.deck = deck;
    }


    public String getCurrplayers() {
        return currPlayers;
    }

    public void setCurrplayers(String currPlayers) {
        this.currPlayers = currPlayers;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }


}