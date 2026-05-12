





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private None kind;
    private String operation;





    private Deck deck;




    private Player player;


    public Card(
        None kind,        String operation    ) {
        this.kind = kind;
        this.operation = operation;
    }


    public None getKind() {
        return kind;
    }

    public void setKind(None kind) {
        this.kind = kind;
    }
    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }
    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}