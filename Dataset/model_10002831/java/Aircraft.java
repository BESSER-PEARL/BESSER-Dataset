





import java.util.List;
import java.util.ArrayList;

public class Aircraft  {

    private None flightState;
    private None state;





    private List<Pilot> pilots;


    public Aircraft(
        None flightState,        None state    ) {
        this.flightState = flightState;
        this.state = state;
        this.pilots = new ArrayList<>();
    }

    public Aircraft(
        None flightState,        None state        ArrayList<Pilot> pilots    ) {
        this.flightState = flightState;
        this.state = state;
        this.pilots = pilots;
    }

    public None getFlightstate() {
        return flightState;
    }

    public void setFlightstate(None flightState) {
        this.flightState = flightState;
    }
    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }

    public List<Pilot> getPilots() {
        return pilots;
    }

    public void addPilot(Pilot pilot) {
        this.pilots.add(pilot);
    }

}