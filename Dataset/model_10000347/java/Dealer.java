





import java.util.List;
import java.util.ArrayList;

public class Dealer  {

    private None deck;
    private None analyzeHand;





    private Deck deck;




    private Poker poker;


    public Dealer(
        None deck,        None analyzeHand    ) {
        this.deck = deck;
        this.analyzeHand = analyzeHand;
    }


    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public None getAnalyzehand() {
        return analyzeHand;
    }

    public void setAnalyzehand(None analyzeHand) {
        this.analyzeHand = analyzeHand;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }
    public Poker getPoker() {
        return poker;
    }

    public void setPoker(Poker poker) {
        this.poker = poker;
    }

}