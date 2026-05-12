





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int ACE;
    private int KING;
    private int QUEEN;
    private int CLUBS;
    private int JACK;
    private int JOKER;
    private int DIAMONDS;
    private int HEARTS;
    private int suit;
    private int SPADES;
    private int value;



    public Card(
        int ACE,        int KING,        int QUEEN,        int CLUBS,        int JACK,        int JOKER,        int DIAMONDS,        int HEARTS,        int suit,        int SPADES,        int value    ) {
        this.ACE = ACE;
        this.KING = KING;
        this.QUEEN = QUEEN;
        this.CLUBS = CLUBS;
        this.JACK = JACK;
        this.JOKER = JOKER;
        this.DIAMONDS = DIAMONDS;
        this.HEARTS = HEARTS;
        this.suit = suit;
        this.SPADES = SPADES;
        this.value = value;
    }


    public int getAce() {
        return ACE;
    }

    public void setAce(int ACE) {
        this.ACE = ACE;
    }
    public int getKing() {
        return KING;
    }

    public void setKing(int KING) {
        this.KING = KING;
    }
    public int getQueen() {
        return QUEEN;
    }

    public void setQueen(int QUEEN) {
        this.QUEEN = QUEEN;
    }
    public int getClubs() {
        return CLUBS;
    }

    public void setClubs(int CLUBS) {
        this.CLUBS = CLUBS;
    }
    public int getJack() {
        return JACK;
    }

    public void setJack(int JACK) {
        this.JACK = JACK;
    }
    public int getJoker() {
        return JOKER;
    }

    public void setJoker(int JOKER) {
        this.JOKER = JOKER;
    }
    public int getDiamonds() {
        return DIAMONDS;
    }

    public void setDiamonds(int DIAMONDS) {
        this.DIAMONDS = DIAMONDS;
    }
    public int getHearts() {
        return HEARTS;
    }

    public void setHearts(int HEARTS) {
        this.HEARTS = HEARTS;
    }
    public int getSuit() {
        return suit;
    }

    public void setSuit(int suit) {
        this.suit = suit;
    }
    public int getSpades() {
        return SPADES;
    }

    public void setSpades(int SPADES) {
        this.SPADES = SPADES;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}