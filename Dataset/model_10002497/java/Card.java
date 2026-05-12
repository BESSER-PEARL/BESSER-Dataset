





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String suit;
    private None kind;





    private Player player;


    public Card(
        String suit,        None kind    ) {
        this.suit = suit;
        this.kind = kind;
    }


    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }
    public None getKind() {
        return kind;
    }

    public void setKind(None kind) {
        this.kind = kind;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}