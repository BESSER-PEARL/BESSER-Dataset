





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private int numWins;
    private int numLose;
    private int numGames;





    private Player player;


    public Game(
        int numWins,        int numLose,        int numGames    ) {
        this.numWins = numWins;
        this.numLose = numLose;
        this.numGames = numGames;
    }


    public int getNumwins() {
        return numWins;
    }

    public void setNumwins(int numWins) {
        this.numWins = numWins;
    }
    public int getNumlose() {
        return numLose;
    }

    public void setNumlose(int numLose) {
        this.numLose = numLose;
    }
    public int getNumgames() {
        return numGames;
    }

    public void setNumgames(int numGames) {
        this.numGames = numGames;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}