





import java.util.List;
import java.util.ArrayList;

public class TransportationProduct  {

    private float distance;
    private String source;
    private String destination;



    public TransportationProduct(
        float distance,        String source,        String destination    ) {
        this.distance = distance;
        this.source = source;
        this.destination = destination;
    }


    public float getDistance() {
        return distance;
    }

    public void setDistance(float distance) {
        this.distance = distance;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }


}