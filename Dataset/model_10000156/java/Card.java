





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private None suit;
    private None kind;





    private Deck deck;




    private Player player;


    public Card(
        None suit,        None kind    ) {
        this.suit = suit;
        this.kind = kind;
    }


    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }
    public None getKind() {
        return kind;
    }

    public void setKind(None kind) {
        this.kind = kind;
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