





import java.util.List;
import java.util.ArrayList;

public class Card_Deck  {

    private String random;
    private int remainder;
    private int decksize;
    private String deck;
    private int handsize;
    private int shuffletimes;



    public Card_Deck(
        String random,        int remainder,        int decksize,        String deck,        int handsize,        int shuffletimes    ) {
        this.random = random;
        this.remainder = remainder;
        this.decksize = decksize;
        this.deck = deck;
        this.handsize = handsize;
        this.shuffletimes = shuffletimes;
    }


    public String getRandom() {
        return random;
    }

    public void setRandom(String random) {
        this.random = random;
    }
    public int getRemainder() {
        return remainder;
    }

    public void setRemainder(int remainder) {
        this.remainder = remainder;
    }
    public int getDecksize() {
        return decksize;
    }

    public void setDecksize(int decksize) {
        this.decksize = decksize;
    }
    public String getDeck() {
        return deck;
    }

    public void setDeck(String deck) {
        this.deck = deck;
    }
    public int getHandsize() {
        return handsize;
    }

    public void setHandsize(int handsize) {
        this.handsize = handsize;
    }
    public int getShuffletimes() {
        return shuffletimes;
    }

    public void setShuffletimes(int shuffletimes) {
        this.shuffletimes = shuffletimes;
    }


}