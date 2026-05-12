





import java.util.List;
import java.util.ArrayList;

public class Card___Abstract__  {

    private int _id;





    private Deck deck;


    public Card___Abstract__(
        int _id    ) {
        this._id = _id;
    }


    public int get_id() {
        return _id;
    }

    public void set_id(int _id) {
        this._id = _id;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}