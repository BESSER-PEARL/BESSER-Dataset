





import java.util.List;
import java.util.ArrayList;

public class Dealer  {

    private None analyzeHand;
    private None deck;





    private Poker poker;




    private Deck deck;


    public Dealer(
        None analyzeHand,        None deck    ) {
        this.analyzeHand = analyzeHand;
        this.deck = deck;
    }


    public None getAnalyzehand() {
        return analyzeHand;
    }

    public void setAnalyzehand(None analyzeHand) {
        this.analyzeHand = analyzeHand;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }

    public Poker getPoker() {
        return poker;
    }

    public void setPoker(Poker poker) {
        this.poker = poker;
    }
    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}