





import java.util.List;
import java.util.ArrayList;

public class BlackjackGame  {

    private int bet;
    private None player;
    private None dealer;
    private None deck;





    private Gambler gambler;




    private Dealer dealer;


    public BlackjackGame(
        int bet,        None player,        None dealer,        None deck    ) {
        this.bet = bet;
        this.player = player;
        this.dealer = dealer;
        this.deck = deck;
    }


    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }
    public None getPlayer() {
        return player;
    }

    public void setPlayer(None player) {
        this.player = player;
    }
    public None getDealer() {
        return dealer;
    }

    public void setDealer(None dealer) {
        this.dealer = dealer;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }

    public Gambler getGambler() {
        return gambler;
    }

    public void setGambler(Gambler gambler) {
        this.gambler = gambler;
    }
    public Dealer getDealer() {
        return dealer;
    }

    public void setDealer(Dealer dealer) {
        this.dealer = dealer;
    }

}