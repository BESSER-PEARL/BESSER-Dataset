





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String rank;
    private String face_up;
    private String suit;



    public Card(
        String rank,        String face_up,        String suit    ) {
        this.rank = rank;
        this.face_up = face_up;
        this.suit = suit;
    }


    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
    }
    public String getFace_up() {
        return face_up;
    }

    public void setFace_up(String face_up) {
        this.face_up = face_up;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }


}