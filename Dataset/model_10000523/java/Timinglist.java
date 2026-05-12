





import java.util.List;
import java.util.ArrayList;

public class Timinglist  {

    private String flightname;
    private String destination;
    private String time;
    private String source;





    private System system;


    public Timinglist(
        String flightname,        String destination,        String time,        String source    ) {
        this.flightname = flightname;
        this.destination = destination;
        this.time = time;
        this.source = source;
    }


    public String getFlightname() {
        return flightname;
    }

    public void setFlightname(String flightname) {
        this.flightname = flightname;
    }
    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}