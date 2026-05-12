





import java.util.List;
import java.util.ArrayList;

public class CardCollection  {

    private String collection;





    private Card card;


    public CardCollection(
        String collection    ) {
        this.collection = collection;
    }


    public String getCollection() {
        return collection;
    }

    public void setCollection(String collection) {
        this.collection = collection;
    }

    public Card getCard() {
        return card;
    }

    public void setCard(Card card) {
        this.card = card;
    }

}