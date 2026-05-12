





import java.util.List;
import java.util.ArrayList;

public class BlackJack  {

    private None playersHand;
    private int money;
    private None dealersHand;
    private int handCount;
    private int bet;
    private None deck;



    public BlackJack(
        None playersHand,        int money,        None dealersHand,        int handCount,        int bet,        None deck    ) {
        this.playersHand = playersHand;
        this.money = money;
        this.dealersHand = dealersHand;
        this.handCount = handCount;
        this.bet = bet;
        this.deck = deck;
    }


    public None getPlayershand() {
        return playersHand;
    }

    public void setPlayershand(None playersHand) {
        this.playersHand = playersHand;
    }
    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }
    public None getDealershand() {
        return dealersHand;
    }

    public void setDealershand(None dealersHand) {
        this.dealersHand = dealersHand;
    }
    public int getHandcount() {
        return handCount;
    }

    public void setHandcount(int handCount) {
        this.handCount = handCount;
    }
    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }


}