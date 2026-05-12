





import java.util.List;
import java.util.ArrayList;

public class entities_Score  {

    private String game;
    private int points;
    private String player;
    private None playedOn;



    public entities_Score(
        String game,        int points,        String player,        None playedOn    ) {
        this.game = game;
        this.points = points;
        this.player = player;
        this.playedOn = playedOn;
    }


    public String getGame() {
        return game;
    }

    public void setGame(String game) {
        this.game = game;
    }
    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }
    public String getPlayer() {
        return player;
    }

    public void setPlayer(String player) {
        this.player = player;
    }
    public None getPlayedon() {
        return playedOn;
    }

    public void setPlayedon(None playedOn) {
        this.playedOn = playedOn;
    }


}