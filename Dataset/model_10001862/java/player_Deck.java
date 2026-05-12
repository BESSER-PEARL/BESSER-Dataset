





import java.util.List;
import java.util.ArrayList;

public class player_Deck  {

    private int remainofDeck;
    private int hand_size;
    private int deck_size;
    private int numberofShuffles;



    public player_Deck(
        int remainofDeck,        int hand_size,        int deck_size,        int numberofShuffles    ) {
        this.remainofDeck = remainofDeck;
        this.hand_size = hand_size;
        this.deck_size = deck_size;
        this.numberofShuffles = numberofShuffles;
    }


    public int getRemainofdeck() {
        return remainofDeck;
    }

    public void setRemainofdeck(int remainofDeck) {
        this.remainofDeck = remainofDeck;
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
    public int getNumberofshuffles() {
        return numberofShuffles;
    }

    public void setNumberofshuffles(int numberofShuffles) {
        this.numberofShuffles = numberofShuffles;
    }


}