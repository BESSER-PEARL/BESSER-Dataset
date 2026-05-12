





import java.util.List;
import java.util.ArrayList;

public class Carte  {

    private String ordre;
    private int suit;



    public Carte(
        String ordre,        int suit    ) {
        this.ordre = ordre;
        this.suit = suit;
    }


    public String getOrdre() {
        return ordre;
    }

    public void setOrdre(String ordre) {
        this.ordre = ordre;
    }
    public int getSuit() {
        return suit;
    }

    public void setSuit(int suit) {
        this.suit = suit;
    }


}