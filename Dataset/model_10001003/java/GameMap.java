





import java.util.List;
import java.util.ArrayList;

public class GameMap  {

    private String walls;
    private String transitions;
    private String poerups;



    public GameMap(
        String walls,        String transitions,        String poerups    ) {
        this.walls = walls;
        this.transitions = transitions;
        this.poerups = poerups;
    }


    public String getWalls() {
        return walls;
    }

    public void setWalls(String walls) {
        this.walls = walls;
    }
    public String getTransitions() {
        return transitions;
    }

    public void setTransitions(String transitions) {
        this.transitions = transitions;
    }
    public String getPoerups() {
        return poerups;
    }

    public void setPoerups(String poerups) {
        this.poerups = poerups;
    }


}