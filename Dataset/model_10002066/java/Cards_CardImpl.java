





import java.util.List;
import java.util.ArrayList;

public class Cards_CardImpl  {

    private boolean isMarked;
    private String Suit;
    private None Cardinality;



    public Cards_CardImpl(
        boolean isMarked,        String Suit,        None Cardinality    ) {
        this.isMarked = isMarked;
        this.Suit = Suit;
        this.Cardinality = Cardinality;
    }


    public boolean getIsmarked() {
        return isMarked;
    }

    public void setIsmarked(boolean isMarked) {
        this.isMarked = isMarked;
    }
    public String getSuit() {
        return Suit;
    }

    public void setSuit(String Suit) {
        this.Suit = Suit;
    }
    public None getCardinality() {
        return Cardinality;
    }

    public void setCardinality(None Cardinality) {
        this.Cardinality = Cardinality;
    }


}