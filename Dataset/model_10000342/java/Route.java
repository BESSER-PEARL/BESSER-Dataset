





import java.util.List;
import java.util.ArrayList;

public class Route  {

    private String source;
    private String destination;
    private String stops;
    private int routeId;





    private Service service;


    public Route(
        String source,        String destination,        String stops,        int routeId    ) {
        this.source = source;
        this.destination = destination;
        this.stops = stops;
        this.routeId = routeId;
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
    public String getStops() {
        return stops;
    }

    public void setStops(String stops) {
        this.stops = stops;
    }
    public int getRouteid() {
        return routeId;
    }

    public void setRouteid(int routeId) {
        this.routeId = routeId;
    }

    public Service getService() {
        return service;
    }

    public void setService(Service service) {
        this.service = service;
    }

}