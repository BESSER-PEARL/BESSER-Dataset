





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private String players;
    private None winner;
    private int round;





    private Deck deck;


    public Game(
        String players,        None winner,        int round    ) {
        this.players = players;
        this.winner = winner;
        this.round = round;
    }


    public String getPlayers() {
        return players;
    }

    public void setPlayers(String players) {
        this.players = players;
    }
    public None getWinner() {
        return winner;
    }

    public void setWinner(None winner) {
        this.winner = winner;
    }
    public int getRound() {
        return round;
    }

    public void setRound(int round) {
        this.round = round;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}