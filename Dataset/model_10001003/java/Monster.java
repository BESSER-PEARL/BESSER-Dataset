





import java.util.List;
import java.util.ArrayList;

public class Monster  {

    private int lives;
    private String location;
    private String specilization;
    private String type;



    public Monster(
        int lives,        String location,        String specilization,        String type    ) {
        this.lives = lives;
        this.location = location;
        this.specilization = specilization;
        this.type = type;
    }


    public int getLives() {
        return lives;
    }

    public void setLives(int lives) {
        this.lives = lives;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getSpecilization() {
        return specilization;
    }

    public void setSpecilization(String specilization) {
        this.specilization = specilization;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}