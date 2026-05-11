





import java.util.List;
import java.util.ArrayList;

public class marsRover_ultra  {

    private int distance;
    private String name;



    public marsRover_ultra(
        int distance,        String name    ) {
        this.distance = distance;
        this.name = name;
    }


    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}