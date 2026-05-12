





import java.util.List;
import java.util.ArrayList;

public class Route  {

    private String source;
    private String stops;
    private int routeId;
    private String destination;





    private Service service;


    public Route(
        String source,        String stops,        int routeId,        String destination    ) {
        this.source = source;
        this.stops = stops;
        this.routeId = routeId;
        this.destination = destination;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
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
    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }

    public Service getService() {
        return service;
    }

    public void setService(Service service) {
        this.service = service;
    }

}