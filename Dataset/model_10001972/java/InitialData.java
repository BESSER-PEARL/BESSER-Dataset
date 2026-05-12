





import java.util.List;
import java.util.ArrayList;

public class InitialData  {

    private String points;
    private String playerName;



    public InitialData(
        String points,        String playerName    ) {
        this.points = points;
        this.playerName = playerName;
    }


    public String getPoints() {
        return points;
    }

    public void setPoints(String points) {
        this.points = points;
    }
    public String getPlayername() {
        return playerName;
    }

    public void setPlayername(String playerName) {
        this.playerName = playerName;
    }


}