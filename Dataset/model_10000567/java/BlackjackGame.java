





import java.util.List;
import java.util.ArrayList;

public class BlackjackGame  {

    private None deck;
    private None player;
    private None dealer;
    private int bet;





    private Dealer dealer;




    private GameView gameview;




    private Player player;


    public BlackjackGame(
        None deck,        None player,        None dealer,        int bet    ) {
        this.deck = deck;
        this.player = player;
        this.dealer = dealer;
        this.bet = bet;
    }


    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
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

    public Dealer getDealer() {
        return dealer;
    }

    public void setDealer(Dealer dealer) {
        this.dealer = dealer;
    }
    public GameView getGameview() {
        return gameview;
    }

    public void setGameview(GameView gameview) {
        this.gameview = gameview;
    }
    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}