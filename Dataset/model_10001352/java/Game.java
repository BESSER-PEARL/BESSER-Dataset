





import java.util.List;
import java.util.ArrayList;

public class Game  {






    private Spectator spectator;




    private Grid grid;




    private List<Player> players;


    public Game(
    ) {
        this.players = new ArrayList<>();
    }

    public Game(
        ArrayList<Player> players    ) {
        this.players = players;
    }


    public Spectator getSpectator() {
        return spectator;
    }

    public void setSpectator(Spectator spectator) {
        this.spectator = spectator;
    }
    public Grid getGrid() {
        return grid;
    }

    public void setGrid(Grid grid) {
        this.grid = grid;
    }
    public List<Player> getPlayers() {
        return players;
    }

    public void addPlayer(Player player) {
        this.players.add(player);
    }

}