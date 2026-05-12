





import java.util.List;
import java.util.ArrayList;

public class Application  {

    private None deck;
    private String scan;



    public Application(
        None deck,        String scan    ) {
        this.deck = deck;
        this.scan = scan;
    }


    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public String getScan() {
        return scan;
    }

    public void setScan(String scan) {
        this.scan = scan;
    }


}