





import java.util.List;
import java.util.ArrayList;

public class Timinglist  {

    private String source;
    private String time;
    private String destination;
    private String flightname;





    private System system;


    public Timinglist(
        String source,        String time,        String destination,        String flightname    ) {
        this.source = source;
        this.time = time;
        this.destination = destination;
        this.flightname = flightname;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }
    public String getFlightname() {
        return flightname;
    }

    public void setFlightname(String flightname) {
        this.flightname = flightname;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}