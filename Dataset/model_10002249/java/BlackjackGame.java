





import java.util.List;
import java.util.ArrayList;

public class BlackjackGame  {

    private None player;
    private None dealer;
    private int bet;
    private None deck;





    private Dealer dealer;




    private Player player;


    public BlackjackGame(
        None player,        None dealer,        int bet,        None deck    ) {
        this.player = player;
        this.dealer = dealer;
        this.bet = bet;
        this.deck = deck;
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

    public Dealer getDealer() {
        return dealer;
    }

    public void setDealer(Dealer dealer) {
        this.dealer = dealer;
    }
    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}