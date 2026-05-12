





import java.util.List;
import java.util.ArrayList;

public class Aircraft  {

    private None state;
    private None flightState;





    private List<Pilot> pilots;




    private List<Flight> flights;




    private List<Airline> airlines;


    public Aircraft(
        None state,        None flightState    ) {
        this.state = state;
        this.flightState = flightState;
        this.pilots = new ArrayList<>();
        this.flights = new ArrayList<>();
        this.airlines = new ArrayList<>();
    }

    public Aircraft(
        None state,        None flightState        ArrayList<Pilot> pilots,        ArrayList<Flight> flights,        ArrayList<Airline> airlines    ) {
        this.state = state;
        this.flightState = flightState;
        this.pilots = pilots;
        this.flights = flights;
        this.airlines = airlines;
    }

    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }
    public None getFlightstate() {
        return flightState;
    }

    public void setFlightstate(None flightState) {
        this.flightState = flightState;
    }

    public List<Pilot> getPilots() {
        return pilots;
    }

    public void addPilot(Pilot pilot) {
        this.pilots.add(pilot);
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

}