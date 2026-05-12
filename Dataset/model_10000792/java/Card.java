





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int value;
    private int rank;
    private String suit;





    private Blackjack blackjack;


    public Card(
        int value,        int rank,        String suit    ) {
        this.value = value;
        this.rank = rank;
        this.suit = suit;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }

    public Blackjack getBlackjack() {
        return blackjack;
    }

    public void setBlackjack(Blackjack blackjack) {
        this.blackjack = blackjack;
    }

}