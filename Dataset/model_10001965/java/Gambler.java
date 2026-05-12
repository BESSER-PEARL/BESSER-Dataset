





import java.util.List;
import java.util.ArrayList;

public class Gambler  {

    private int bet;
    private String hands;
    private boolean hasSplit;





    private List<BlackJackHandDeck> blackjackhanddecks;


    public Gambler(
        int bet,        String hands,        boolean hasSplit    ) {
        this.bet = bet;
        this.hands = hands;
        this.hasSplit = hasSplit;
        this.blackjackhanddecks = new ArrayList<>();
    }

    public Gambler(
        int bet,        String hands,        boolean hasSplit        ArrayList<BlackJackHandDeck> blackjackhanddecks    ) {
        this.bet = bet;
        this.hands = hands;
        this.hasSplit = hasSplit;
        this.blackjackhanddecks = blackjackhanddecks;
    }

    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }
    public String getHands() {
        return hands;
    }

    public void setHands(String hands) {
        this.hands = hands;
    }
    public boolean getHassplit() {
        return hasSplit;
    }

    public void setHassplit(boolean hasSplit) {
        this.hasSplit = hasSplit;
    }

    public List<BlackJackHandDeck> getBlackjackhanddecks() {
        return blackjackhanddecks;
    }

    public void addBlackjackhanddeck(Blackjackhanddeck blackjackhanddeck) {
        this.blackjackhanddecks.add(blackjackhanddeck);
    }

}