





import java.util.List;
import java.util.ArrayList;

public class FortuneTeller  {

    private None _tarotDeck;





    private Deck deck;


    public FortuneTeller(
        None _tarotDeck    ) {
        this._tarotDeck = _tarotDeck;
    }


    public None get_tarotdeck() {
        return _tarotDeck;
    }

    public void set_tarotdeck(None _tarotDeck) {
        this._tarotDeck = _tarotDeck;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}