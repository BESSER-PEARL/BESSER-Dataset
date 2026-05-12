





import java.util.List;
import java.util.ArrayList;

public class Players_Player  {

    private None Hand;
    private None chips;
    private boolean isSmallBlind;
    private boolean hasFolded;
    private boolean isDealer;
    private boolean isBigBlind;





    private Cards_Deck cards_deck;


    public Players_Player(
        None Hand,        None chips,        boolean isSmallBlind,        boolean hasFolded,        boolean isDealer,        boolean isBigBlind    ) {
        this.Hand = Hand;
        this.chips = chips;
        this.isSmallBlind = isSmallBlind;
        this.hasFolded = hasFolded;
        this.isDealer = isDealer;
        this.isBigBlind = isBigBlind;
    }


    public None getHand() {
        return Hand;
    }

    public void setHand(None Hand) {
        this.Hand = Hand;
    }
    public None getChips() {
        return chips;
    }

    public void setChips(None chips) {
        this.chips = chips;
    }
    public boolean getIssmallblind() {
        return isSmallBlind;
    }

    public void setIssmallblind(boolean isSmallBlind) {
        this.isSmallBlind = isSmallBlind;
    }
    public boolean getHasfolded() {
        return hasFolded;
    }

    public void setHasfolded(boolean hasFolded) {
        this.hasFolded = hasFolded;
    }
    public boolean getIsdealer() {
        return isDealer;
    }

    public void setIsdealer(boolean isDealer) {
        this.isDealer = isDealer;
    }
    public boolean getIsbigblind() {
        return isBigBlind;
    }

    public void setIsbigblind(boolean isBigBlind) {
        this.isBigBlind = isBigBlind;
    }

    public Cards_Deck getCards_deck() {
        return cards_deck;
    }

    public void setCards_deck(Cards_Deck cards_deck) {
        this.cards_deck = cards_deck;
    }

}