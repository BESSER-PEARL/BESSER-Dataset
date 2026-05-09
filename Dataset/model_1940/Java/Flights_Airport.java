





import java.util.List;
import java.util.ArrayList;

public class Flights_Airport extends FlightObject {

    private float size;





    private Flights_Airports flights_airports;




    private List<Flights_Route> flights_routes;




    private Flights_Route flights_route;




    private List<Flights_Route> flights_routes;




    private Flights_Route flights_route;




    private List<Flights_Gate> flights_gates;


    public Flights_Airport(
        float size    ) {
        super(
        );
        this.size = size;
        this.flights_routes = new ArrayList<>();
        this.flights_routes = new ArrayList<>();
        this.flights_gates = new ArrayList<>();
    }

    public Flights_Airport(
        float size        ArrayList<Flights_Route> flights_routes,        ArrayList<Flights_Route> flights_routes,        ArrayList<Flights_Gate> flights_gates    ) {
        this.size = size;
        this.flights_routes = flights_routes;
        this.flights_routes = flights_routes;
        this.flights_gates = flights_gates;
    }

    public float getSize() {
        return size;
    }

    public void setSize(float size) {
        this.size = size;
    }

    public Flights_Airports getFlights_airports() {
        return flights_airports;
    }

    public void setFlights_airports(Flights_Airports flights_airports) {
        this.flights_airports = flights_airports;
    }
    public List<Flights_Route> getFlights_routes() {
        return flights_routes;
    }

    public void addFlights_route(Flights_route flights_route) {
        this.flights_routes.add(flights_route);
    }
    public Flights_Route getFlights_route() {
        return flights_route;
    }

    public void setFlights_route(Flights_Route flights_route) {
        this.flights_route = flights_route;
    }
    public List<Flights_Route> getFlights_routes() {
        return flights_routes;
    }

    public void addFlights_route(Flights_route flights_route) {
        this.flights_routes.add(flights_route);
    }
    public Flights_Route getFlights_route() {
        return flights_route;
    }

    public void setFlights_route(Flights_Route flights_route) {
        this.flights_route = flights_route;
    }
    public List<Flights_Gate> getFlights_gates() {
        return flights_gates;
    }

    public void addFlights_gate(Flights_gate flights_gate) {
        this.flights_gates.add(flights_gate);
    }

}