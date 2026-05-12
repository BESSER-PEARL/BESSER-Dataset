





import java.util.List;
import java.util.ArrayList;

public class Aircraft  {

    private None state;
    private None flightState;





    private List<Airline> airlines;




    private List<Pilot> pilots;




    private List<Flight> flights;


    public Aircraft(
        None state,        None flightState    ) {
        this.state = state;
        this.flightState = flightState;
        this.airlines = new ArrayList<>();
        this.pilots = new ArrayList<>();
        this.flights = new ArrayList<>();
    }

    public Aircraft(
        None state,        None flightState        ArrayList<Airline> airlines,        ArrayList<Pilot> pilots,        ArrayList<Flight> flights    ) {
        this.state = state;
        this.flightState = flightState;
        this.airlines = airlines;
        this.pilots = pilots;
        this.flights = flights;
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
    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        this.flights.add(flight);
    }

}