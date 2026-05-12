





import java.util.List;
import java.util.ArrayList;

public class Aircraft  {

    private None flightState;
    private None state;





    private List<Flight> flights;




    private List<Airline> airlines;




    private List<Pilot> pilots;


    public Aircraft(
        None flightState,        None state    ) {
        this.flightState = flightState;
        this.state = state;
        this.flights = new ArrayList<>();
        this.airlines = new ArrayList<>();
        this.pilots = new ArrayList<>();
    }

    public Aircraft(
        None flightState,        None state        ArrayList<Flight> flights,        ArrayList<Airline> airlines,        ArrayList<Pilot> pilots    ) {
        this.flightState = flightState;
        this.state = state;
        this.flights = flights;
        this.airlines = airlines;
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

    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        this.flights.add(flight);
    }
    public List<Airline> getAirlines() {
        return airlines;
    }

    public void addAirline(Airline airline) {
        this.airlines.add(airline);
    }
    public List<Pilot> getPilots() {
        return pilots;
    }

    public void addPilot(Pilot pilot) {
        this.pilots.add(pilot);
    }

}