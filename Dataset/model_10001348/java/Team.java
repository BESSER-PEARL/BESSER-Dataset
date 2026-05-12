





import java.util.List;
import java.util.ArrayList;

public class Team  {

    private None p2;
    private int score;
    private None p1;





    private Player player;


    public Team(
        None p2,        int score,        None p1    ) {
        this.p2 = p2;
        this.score = score;
        this.p1 = p1;
    }


    public None getP2() {
        return p2;
    }

    public void setP2(None p2) {
        this.p2 = p2;
    }
    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
    public None getP1() {
        return p1;
    }

    public void setP1(None p1) {
        this.p1 = p1;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}