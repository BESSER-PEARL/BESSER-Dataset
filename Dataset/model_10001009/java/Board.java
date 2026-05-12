





import java.util.List;
import java.util.ArrayList;

public class Board  {






    private List<Player> players;


    public Board(
    ) {
        this.players = new ArrayList<>();
    }

    public Board(
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