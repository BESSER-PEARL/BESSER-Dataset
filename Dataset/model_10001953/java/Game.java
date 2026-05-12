





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private None winner;





    private List<Player> players;




    private Dealer dealer;


    public Game(
        None winner    ) {
        this.winner = winner;
        this.players = new ArrayList<>();
    }

    public Game(
        None winner        ArrayList<Player> players    ) {
        this.winner = winner;
        this.players = players;
    }

    public None getWinner() {
        return winner;
    }

    public void setWinner(None winner) {
        this.winner = winner;
    }

    public List<Player> getPlayers() {
        return players;
    }

    public void addPlayer(Player player) {
        this.players.add(player);
    }
    public Dealer getDealer() {
        return dealer;
    }

    public void setDealer(Dealer dealer) {
        this.dealer = dealer;
    }

}