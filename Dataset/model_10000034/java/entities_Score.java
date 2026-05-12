





import java.util.List;
import java.util.ArrayList;

public class entities_Score  {

    private int points;
    private String game;
    private None playedOn;
    private String player;



    public entities_Score(
        int points,        String game,        None playedOn,        String player    ) {
        this.points = points;
        this.game = game;
        this.playedOn = playedOn;
        this.player = player;
    }


    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }
    public String getGame() {
        return game;
    }

    public void setGame(String game) {
        this.game = game;
    }
    public None getPlayedon() {
        return playedOn;
    }

    public void setPlayedon(None playedOn) {
        this.playedOn = playedOn;
    }
    public String getPlayer() {
        return player;
    }

    public void setPlayer(String player) {
        this.player = player;
    }


}