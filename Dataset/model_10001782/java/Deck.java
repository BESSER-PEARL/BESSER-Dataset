





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private int Deck_ArrayList_;
    private int Topcard;



    public Deck(
        int Deck_ArrayList_,        int Topcard    ) {
        this.Deck_ArrayList_ = Deck_ArrayList_;
        this.Topcard = Topcard;
    }


    public int getDeck_arraylist_() {
        return Deck_ArrayList_;
    }

    public void setDeck_arraylist_(int Deck_ArrayList_) {
        this.Deck_ArrayList_ = Deck_ArrayList_;
    }
    public int getTopcard() {
        return Topcard;
    }

    public void setTopcard(int Topcard) {
        this.Topcard = Topcard;
    }


}