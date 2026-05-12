





import java.util.List;
import java.util.ArrayList;

public class CardGame  {

    private int round;
    private None winner;
    private String players;





    private Deck deck;


    public CardGame(
        int round,        None winner,        String players    ) {
        this.round = round;
        this.winner = winner;
        this.players = players;
    }


    public int getRound() {
        return round;
    }

    public void setRound(int round) {
        this.round = round;
    }
    public None getWinner() {
        return winner;
    }

    public void setWinner(None winner) {
        this.winner = winner;
    }
    public String getPlayers() {
        return players;
    }

    public void setPlayers(String players) {
        this.players = players;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}