





import java.util.List;
import java.util.ArrayList;

public class Poker_Hand  {

    private int numCards;
    private boolean Fold;
    private None handIterator;
    private String cardsInHand;





    private Poker_HandIterator poker_handiterator;


    public Poker_Hand(
        int numCards,        boolean Fold,        None handIterator,        String cardsInHand    ) {
        this.numCards = numCards;
        this.Fold = Fold;
        this.handIterator = handIterator;
        this.cardsInHand = cardsInHand;
    }


    public int getNumcards() {
        return numCards;
    }

    public void setNumcards(int numCards) {
        this.numCards = numCards;
    }
    public boolean getFold() {
        return Fold;
    }

    public void setFold(boolean Fold) {
        this.Fold = Fold;
    }
    public None getHanditerator() {
        return handIterator;
    }

    public void setHanditerator(None handIterator) {
        this.handIterator = handIterator;
    }
    public String getCardsinhand() {
        return cardsInHand;
    }

    public void setCardsinhand(String cardsInHand) {
        this.cardsInHand = cardsInHand;
    }

    public Poker_HandIterator getPoker_handiterator() {
        return poker_handiterator;
    }

    public void setPoker_handiterator(Poker_HandIterator poker_handiterator) {
        this.poker_handiterator = poker_handiterator;
    }

}