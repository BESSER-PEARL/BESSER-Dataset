





import java.util.List;
import java.util.ArrayList;

public class Blackjack  {

    private None cards;
    private String players;
    private None dealer;





    private Player player;


    public Blackjack(
        None cards,        String players,        None dealer    ) {
        this.cards = cards;
        this.players = players;
        this.dealer = dealer;
    }


    public None getCards() {
        return cards;
    }

    public void setCards(None cards) {
        this.cards = cards;
    }
    public String getPlayers() {
        return players;
    }

    public void setPlayers(String players) {
        this.players = players;
    }
    public None getDealer() {
        return dealer;
    }

    public void setDealer(None dealer) {
        this.dealer = dealer;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}