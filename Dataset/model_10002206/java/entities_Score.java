





import java.util.List;
import java.util.ArrayList;

public class entities_Score  {

    private None playedOn;
    private String player;
    private String game;
    private int points;



    public entities_Score(
        None playedOn,        String player,        String game,        int points    ) {
        this.playedOn = playedOn;
        this.player = player;
        this.game = game;
        this.points = points;
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


}