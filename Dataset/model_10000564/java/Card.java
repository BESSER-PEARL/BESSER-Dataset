





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String rank;
    private int suit;





    private Main main;


    public Card(
        String rank,        int suit    ) {
        this.rank = rank;
        this.suit = suit;
    }


    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
    }
    public int getSuit() {
        return suit;
    }

    public void setSuit(int suit) {
        this.suit = suit;
    }

    public Main getMain() {
        return main;
    }

    public void setMain(Main main) {
        this.main = main;
    }

}