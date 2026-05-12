





import java.util.List;
import java.util.ArrayList;

public class BlackjackGame  {

    private int bet;
    private None dealer;
    private None player;
    private None deck;





    private Strategy strategy;




    private GameView gameview;




    private Player player;




    private Dealer dealer;


    public BlackjackGame(
        int bet,        None dealer,        None player,        None deck    ) {
        this.bet = bet;
        this.dealer = dealer;
        this.player = player;
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

    public Strategy getStrategy() {
        return strategy;
    }

    public void setStrategy(Strategy strategy) {
        this.strategy = strategy;
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
    public Dealer getDealer() {
        return dealer;
    }

    public void setDealer(Dealer dealer) {
        this.dealer = dealer;
    }

}