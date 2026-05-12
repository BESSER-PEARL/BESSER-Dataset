





import java.util.List;
import java.util.ArrayList;

public class BomberMan  {

    private int lives;
    private int points;
    private String location;



    public BomberMan(
        int lives,        int points,        String location    ) {
        this.lives = lives;
        this.points = points;
        this.location = location;
    }


    public int getLives() {
        return lives;
    }

    public void setLives(int lives) {
        this.lives = lives;
    }
    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}