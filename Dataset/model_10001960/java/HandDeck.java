





import java.util.List;
import java.util.ArrayList;

public class HandDeck  {

    private boolean naturalBlackJack;
    private boolean pair;
    private boolean stand;
    private boolean bust;



    public HandDeck(
        boolean naturalBlackJack,        boolean pair,        boolean stand,        boolean bust    ) {
        this.naturalBlackJack = naturalBlackJack;
        this.pair = pair;
        this.stand = stand;
        this.bust = bust;
    }


    public boolean getNaturalblackjack() {
        return naturalBlackJack;
    }

    public void setNaturalblackjack(boolean naturalBlackJack) {
        this.naturalBlackJack = naturalBlackJack;
    }
    public boolean getPair() {
        return pair;
    }

    public void setPair(boolean pair) {
        this.pair = pair;
    }
    public boolean getStand() {
        return stand;
    }

    public void setStand(boolean stand) {
        this.stand = stand;
    }
    public boolean getBust() {
        return bust;
    }

    public void setBust(boolean bust) {
        this.bust = bust;
    }


}