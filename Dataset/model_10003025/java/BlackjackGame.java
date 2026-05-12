





import java.util.List;
import java.util.ArrayList;

public class BlackjackGame  {

    private int bet;
    private None deck;
    private None dealer;
    private None player;





    private Dealer dealer;




    private GameView gameview;




    private Player player;


    public BlackjackGame(
        int bet,        None deck,        None dealer,        None player    ) {
        this.bet = bet;
        this.deck = deck;
        this.dealer = dealer;
        this.player = player;
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
    public None getDealer() {
        return dealer;
    }

    public void setDealer(None dealer) {
        this.dealer = dealer;
    }
    public None getPlayer() {
        return player;
    }

    public void setPlayer(None player) {
        this.player = player;
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