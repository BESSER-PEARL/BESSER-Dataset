





import java.util.List;
import java.util.ArrayList;

public class Gameplay_Game  {

    private None pot;
    private int round;
    private String deck;
    private None players;



    public Gameplay_Game(
        None pot,        int round,        String deck,        None players    ) {
        this.pot = pot;
        this.round = round;
        this.deck = deck;
        this.players = players;
    }


    public None getPot() {
        return pot;
    }

    public void setPot(None pot) {
        this.pot = pot;
    }
    public int getRound() {
        return round;
    }

    public void setRound(int round) {
        this.round = round;
    }
    public String getDeck() {
        return deck;
    }

    public void setDeck(String deck) {
        this.deck = deck;
    }
    public None getPlayers() {
        return players;
    }

    public void setPlayers(None players) {
        this.players = players;
    }


}