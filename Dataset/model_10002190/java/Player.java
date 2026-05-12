





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String cards;
    private String type;
    private String value;





    private List<Card> cards;


    public Player(
        String cards,        String type,        String value    ) {
        this.cards = cards;
        this.type = type;
        this.value = value;
        this.cards = new ArrayList<>();
    }

    public Player(
        String cards,        String type,        String value        ArrayList<Card> cards    ) {
        this.cards = cards;
        this.type = type;
        this.value = value;
        this.cards = cards;
    }

    public String getCards() {
        return cards;
    }

    public void setCards(String cards) {
        this.cards = cards;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}