





import java.util.List;
import java.util.ArrayList;

public class Cards_CardImpl  {

    private boolean isMarked;
    private None Cardinality;
    private String Suit;



    public Cards_CardImpl(
        boolean isMarked,        None Cardinality,        String Suit    ) {
        this.isMarked = isMarked;
        this.Cardinality = Cardinality;
        this.Suit = Suit;
    }


    public boolean getIsmarked() {
        return isMarked;
    }

    public void setIsmarked(boolean isMarked) {
        this.isMarked = isMarked;
    }
    public None getCardinality() {
        return Cardinality;
    }

    public void setCardinality(None Cardinality) {
        this.Cardinality = Cardinality;
    }
    public String getSuit() {
        return Suit;
    }

    public void setSuit(String Suit) {
        this.Suit = Suit;
    }


}