





import java.util.List;
import java.util.ArrayList;

public class Route  {

    private String destination;
    private String source;
    private int routeId;
    private String stops;





    private Service service;


    public Route(
        String destination,        String source,        int routeId,        String stops    ) {
        this.destination = destination;
        this.source = source;
        this.routeId = routeId;
        this.stops = stops;
    }


    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public int getRouteid() {
        return routeId;
    }

    public void setRouteid(int routeId) {
        this.routeId = routeId;
    }
    public String getStops() {
        return stops;
    }

    public void setStops(String stops) {
        this.stops = stops;
    }

    public Service getService() {
        return service;
    }

    public void setService(Service service) {
        this.service = service;
    }

}