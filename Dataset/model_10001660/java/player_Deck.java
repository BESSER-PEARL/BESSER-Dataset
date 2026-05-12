





import java.util.List;
import java.util.ArrayList;

public class player_Deck  {

    private int remainofDeck;
    private int numberofShuffles;
    private int hand_size;
    private int deck_size;



    public player_Deck(
        int remainofDeck,        int numberofShuffles,        int hand_size,        int deck_size    ) {
        this.remainofDeck = remainofDeck;
        this.numberofShuffles = numberofShuffles;
        this.hand_size = hand_size;
        this.deck_size = deck_size;
    }


    public int getRemainofdeck() {
        return remainofDeck;
    }

    public void setRemainofdeck(int remainofDeck) {
        this.remainofDeck = remainofDeck;
    }
    public int getNumberofshuffles() {
        return numberofShuffles;
    }

    public void setNumberofshuffles(int numberofShuffles) {
        this.numberofShuffles = numberofShuffles;
    }
    public int getHand_size() {
        return hand_size;
    }

    public void setHand_size(int hand_size) {
        this.hand_size = hand_size;
    }
    public int getDeck_size() {
        return deck_size;
    }

    public void setDeck_size(int deck_size) {
        this.deck_size = deck_size;
    }


}