





import java.util.List;
import java.util.ArrayList;

public class BlackjackGame  {

    private None player;
    private int bet;
    private None dealer;
    private None deck;





    private Player player;




    private GameView gameview;




    private Dealer dealer;


    public BlackjackGame(
        None player,        int bet,        None dealer,        None deck    ) {
        this.player = player;
        this.bet = bet;
        this.dealer = dealer;
        this.deck = deck;
    }


    public None getPlayer() {
        return player;
    }

    public void setPlayer(None player) {
        this.player = player;
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
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
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
    public Dealer getDealer() {
        return dealer;
    }

    public void setDealer(Dealer dealer) {
        this.dealer = dealer;
    }

}