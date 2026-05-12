





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String cardNames;
    private String name;
    private None suit;



    public Card(
        String cardNames,        String name,        None suit    ) {
        this.cardNames = cardNames;
        this.name = name;
        this.suit = suit;
    }


    public String getCardnames() {
        return cardNames;
    }

    public void setCardnames(String cardNames) {
        this.cardNames = cardNames;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }


}