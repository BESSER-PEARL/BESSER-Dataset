





import java.util.List;
import java.util.ArrayList;

public class Poker_Player  {

    private int currentBet;
    private None hand;
    private int currentMoney;



    public Poker_Player(
        int currentBet,        None hand,        int currentMoney    ) {
        this.currentBet = currentBet;
        this.hand = hand;
        this.currentMoney = currentMoney;
    }


    public int getCurrentbet() {
        return currentBet;
    }

    public void setCurrentbet(int currentBet) {
        this.currentBet = currentBet;
    }
    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }
    public int getCurrentmoney() {
        return currentMoney;
    }

    public void setCurrentmoney(int currentMoney) {
        this.currentMoney = currentMoney;
    }


}