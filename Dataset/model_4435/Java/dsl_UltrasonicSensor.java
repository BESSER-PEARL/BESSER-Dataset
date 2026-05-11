





import java.util.List;
import java.util.ArrayList;

public class dsl_UltrasonicSensor extends SensorType {

    private String comparator;
    private String distance;



    public dsl_UltrasonicSensor(
        String comparator,        String distance    ) {
        super(
        );
        this.comparator = comparator;
        this.distance = distance;
    }


    public String getComparator() {
        return comparator;
    }

    public void setComparator(String comparator) {
        this.comparator = comparator;
    }
    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }


}