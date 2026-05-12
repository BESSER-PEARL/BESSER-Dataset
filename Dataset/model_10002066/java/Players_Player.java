





import java.util.List;
import java.util.ArrayList;

public class Players_Player  {

    private boolean isSmallBlind;
    private boolean isDealer;
    private boolean hasFolded;
    private None chips;
    private boolean isBigBlind;
    private None Hand;





    private Cards_Deck cards_deck;


    public Players_Player(
        boolean isSmallBlind,        boolean isDealer,        boolean hasFolded,        None chips,        boolean isBigBlind,        None Hand    ) {
        this.isSmallBlind = isSmallBlind;
        this.isDealer = isDealer;
        this.hasFolded = hasFolded;
        this.chips = chips;
        this.isBigBlind = isBigBlind;
        this.Hand = Hand;
    }


    public boolean getIssmallblind() {
        return isSmallBlind;
    }

    public void setIssmallblind(boolean isSmallBlind) {
        this.isSmallBlind = isSmallBlind;
    }
    public boolean getIsdealer() {
        return isDealer;
    }

    public void setIsdealer(boolean isDealer) {
        this.isDealer = isDealer;
    }
    public boolean getHasfolded() {
        return hasFolded;
    }

    public void setHasfolded(boolean hasFolded) {
        this.hasFolded = hasFolded;
    }
    public None getChips() {
        return chips;
    }

    public void setChips(None chips) {
        this.chips = chips;
    }
    public boolean getIsbigblind() {
        return isBigBlind;
    }

    public void setIsbigblind(boolean isBigBlind) {
        this.isBigBlind = isBigBlind;
    }
    public None getHand() {
        return Hand;
    }

    public void setHand(None Hand) {
        this.Hand = Hand;
    }

    public Cards_Deck getCards_deck() {
        return cards_deck;
    }

    public void setCards_deck(Cards_Deck cards_deck) {
        this.cards_deck = cards_deck;
    }

}