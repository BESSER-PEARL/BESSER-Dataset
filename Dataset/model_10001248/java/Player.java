





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private boolean isAI;
    private boolean isAllIn;
    private int chips;
    private boolean isBigBlind;
    private int playerNumber;
    private boolean isSmallBlind;
    private boolean isFolded;
    private String name;
    private int handValue;
    private String hand;





    private Card card;


    public Player(
        boolean isAI,        boolean isAllIn,        int chips,        boolean isBigBlind,        int playerNumber,        boolean isSmallBlind,        boolean isFolded,        String name,        int handValue,        String hand    ) {
        this.isAI = isAI;
        this.isAllIn = isAllIn;
        this.chips = chips;
        this.isBigBlind = isBigBlind;
        this.playerNumber = playerNumber;
        this.isSmallBlind = isSmallBlind;
        this.isFolded = isFolded;
        this.name = name;
        this.handValue = handValue;
        this.hand = hand;
    }


    public boolean getIsai() {
        return isAI;
    }

    public void setIsai(boolean isAI) {
        this.isAI = isAI;
    }
    public boolean getIsallin() {
        return isAllIn;
    }

    public void setIsallin(boolean isAllIn) {
        this.isAllIn = isAllIn;
    }
    public int getChips() {
        return chips;
    }

    public void setChips(int chips) {
        this.chips = chips;
    }
    public boolean getIsbigblind() {
        return isBigBlind;
    }

    public void setIsbigblind(boolean isBigBlind) {
        this.isBigBlind = isBigBlind;
    }
    public int getPlayernumber() {
        return playerNumber;
    }

    public void setPlayernumber(int playerNumber) {
        this.playerNumber = playerNumber;
    }
    public boolean getIssmallblind() {
        return isSmallBlind;
    }

    public void setIssmallblind(boolean isSmallBlind) {
        this.isSmallBlind = isSmallBlind;
    }
    public boolean getIsfolded() {
        return isFolded;
    }

    public void setIsfolded(boolean isFolded) {
        this.isFolded = isFolded;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getHandvalue() {
        return handValue;
    }

    public void setHandvalue(int handValue) {
        this.handValue = handValue;
    }
    public String getHand() {
        return hand;
    }

    public void setHand(String hand) {
        this.hand = hand;
    }

    public Card getCard() {
        return card;
    }

    public void setCard(Card card) {
        this.card = card;
    }

}