





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String value_dict;





    private Cards cards;


    public Card(
        String value_dict    ) {
        this.value_dict = value_dict;
    }


    public String getValue_dict() {
        return value_dict;
    }

    public void setValue_dict(String value_dict) {
        this.value_dict = value_dict;
    }

    public Cards getCards() {
        return cards;
    }

    public void setCards(Cards cards) {
        this.cards = cards;
    }

}