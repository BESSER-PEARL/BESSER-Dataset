





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private None suit;
    private None color;
    private None rank;





    private Player player;


    public Card(
        None suit,        None color,        None rank    ) {
        this.suit = suit;
        this.color = color;
        this.rank = rank;
    }


    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }
    public None getColor() {
        return color;
    }

    public void setColor(None color) {
        this.color = color;
    }
    public None getRank() {
        return rank;
    }

    public void setRank(None rank) {
        this.rank = rank;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}