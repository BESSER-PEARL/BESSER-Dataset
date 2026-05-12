





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private None p1;
    private boolean done;
    private None p2;





    private List<Player> players;


    public Game(
        None p1,        boolean done,        None p2    ) {
        this.p1 = p1;
        this.done = done;
        this.p2 = p2;
        this.players = new ArrayList<>();
    }

    public Game(
        None p1,        boolean done,        None p2        ArrayList<Player> players    ) {
        this.p1 = p1;
        this.done = done;
        this.p2 = p2;
        this.players = players;
    }

    public None getP1() {
        return p1;
    }

    public void setP1(None p1) {
        this.p1 = p1;
    }
    public boolean getDone() {
        return done;
    }

    public void setDone(boolean done) {
        this.done = done;
    }
    public None getP2() {
        return p2;
    }

    public void setP2(None p2) {
        this.p2 = p2;
    }

    public List<Player> getPlayers() {
        return players;
    }

    public void addPlayer(Player player) {
        this.players.add(player);
    }

}