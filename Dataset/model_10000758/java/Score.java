





import java.util.List;
import java.util.ArrayList;

public class Score  {






    private List<Player> players;


    public Score(
    ) {
        this.players = new ArrayList<>();
    }

    public Score(
        ArrayList<Player> players    ) {
        this.players = players;
    }


    public List<Player> getPlayers() {
        return players;
    }

    public void addPlayer(Player player) {
        this.players.add(player);
    }

}