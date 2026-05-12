





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String Clubs;
    private int Jack_11;
    private String Spades;
    private String suit;
    private int Ace___14;
    private String Hearts;
    private int face;
    private int King_13;
    private int Queen_12;
    private String Diamonds;



    public Card(
        String Clubs,        int Jack_11,        String Spades,        String suit,        int Ace___14,        String Hearts,        int face,        int King_13,        int Queen_12,        String Diamonds    ) {
        this.Clubs = Clubs;
        this.Jack_11 = Jack_11;
        this.Spades = Spades;
        this.suit = suit;
        this.Ace___14 = Ace___14;
        this.Hearts = Hearts;
        this.face = face;
        this.King_13 = King_13;
        this.Queen_12 = Queen_12;
        this.Diamonds = Diamonds;
    }


    public String getClubs() {
        return Clubs;
    }

    public void setClubs(String Clubs) {
        this.Clubs = Clubs;
    }
    public int getJack_11() {
        return Jack_11;
    }

    public void setJack_11(int Jack_11) {
        this.Jack_11 = Jack_11;
    }
    public String getSpades() {
        return Spades;
    }

    public void setSpades(String Spades) {
        this.Spades = Spades;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }
    public int getAce___14() {
        return Ace___14;
    }

    public void setAce___14(int Ace___14) {
        this.Ace___14 = Ace___14;
    }
    public String getHearts() {
        return Hearts;
    }

    public void setHearts(String Hearts) {
        this.Hearts = Hearts;
    }
    public int getFace() {
        return face;
    }

    public void setFace(int face) {
        this.face = face;
    }
    public int getKing_13() {
        return King_13;
    }

    public void setKing_13(int King_13) {
        this.King_13 = King_13;
    }
    public int getQueen_12() {
        return Queen_12;
    }

    public void setQueen_12(int Queen_12) {
        this.Queen_12 = Queen_12;
    }
    public String getDiamonds() {
        return Diamonds;
    }

    public void setDiamonds(String Diamonds) {
        this.Diamonds = Diamonds;
    }


}