





import java.util.List;
import java.util.ArrayList;

public class BlackjackGame  {

    private None player;
    private None deck;
    private int bet;
    private None dealer;





    private Dealer dealer;




    private Player player;




    private GameView gameview;


    public BlackjackGame(
        None player,        None deck,        int bet,        None dealer    ) {
        this.player = player;
        this.deck = deck;
        this.bet = bet;
        this.dealer = dealer;
    }


    public None getPlayer() {
        return player;
    }

    public void setPlayer(None player) {
        this.player = player;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }
    public None getDealer() {
        return dealer;
    }

    public void setDealer(None dealer) {
        this.dealer = dealer;
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
    public GameView getGameview() {
        return gameview;
    }

    public void setGameview(GameView gameview) {
        this.gameview = gameview;
    }

}