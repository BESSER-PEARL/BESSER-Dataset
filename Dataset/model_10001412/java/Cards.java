





import java.util.List;
import java.util.ArrayList;

public class Cards  {

    private String int;
    private String bool;
    private String int1;
    private String string;





    private Deck deck;


    public Cards(
        String int,        String bool,        String int1,        String string    ) {
        this.int = int;
        this.bool = bool;
        this.int1 = int1;
        this.string = string;
    }


    public String getInt() {
        return int;
    }

    public void setInt(String int) {
        this.int = int;
    }
    public String getBool() {
        return bool;
    }

    public void setBool(String bool) {
        this.bool = bool;
    }
    public String getInt1() {
        return int1;
    }

    public void setInt1(String int1) {
        this.int1 = int1;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}