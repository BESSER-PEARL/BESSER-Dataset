





import java.util.List;
import java.util.ArrayList;

public class PowerUps  {

    private String speciliaty;
    private int points;
    private String locations;



    public PowerUps(
        String speciliaty,        int points,        String locations    ) {
        this.speciliaty = speciliaty;
        this.points = points;
        this.locations = locations;
    }


    public String getSpeciliaty() {
        return speciliaty;
    }

    public void setSpeciliaty(String speciliaty) {
        this.speciliaty = speciliaty;
    }
    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }
    public String getLocations() {
        return locations;
    }

    public void setLocations(String locations) {
        this.locations = locations;
    }


}