





import java.util.List;
import java.util.ArrayList;

public class HandDeck  {

    private int total;
    private None cards;





    private Dealer dealer;




    private Gambler gambler;


    public HandDeck(
        int total,        None cards    ) {
        this.total = total;
        this.cards = cards;
    }


    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }
    public None getCards() {
        return cards;
    }

    public void setCards(None cards) {
        this.cards = cards;
    }

    public Dealer getDealer() {
        return dealer;
    }

    public void setDealer(Dealer dealer) {
        this.dealer = dealer;
    }
    public Gambler getGambler() {
        return gambler;
    }

    public void setGambler(Gambler gambler) {
        this.gambler = gambler;
    }

}