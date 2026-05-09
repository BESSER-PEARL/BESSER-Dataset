





import java.util.List;
import java.util.ArrayList;

public class Flights_Flight extends FlightObject {

    private String newAttribute;





    private Flights_TimeStamp flights_timestamp;




    private Flights_FlightContainer flights_flightcontainer;




    private Flights_TimeStamp flights_timestamp;


    public Flights_Flight(
        String newAttribute    ) {
        super(
        );
        this.newAttribute = newAttribute;
    }


    public String getNewattribute() {
        return newAttribute;
    }

    public void setNewattribute(String newAttribute) {
        this.newAttribute = newAttribute;
    }

    public Flights_TimeStamp getFlights_timestamp() {
        return flights_timestamp;
    }

    public void setFlights_timestamp(Flights_TimeStamp flights_timestamp) {
        this.flights_timestamp = flights_timestamp;
    }
    public Flights_FlightContainer getFlights_flightcontainer() {
        return flights_flightcontainer;
    }

    public void setFlights_flightcontainer(Flights_FlightContainer flights_flightcontainer) {
        this.flights_flightcontainer = flights_flightcontainer;
    }
    public Flights_TimeStamp getFlights_timestamp() {
        return flights_timestamp;
    }

    public void setFlights_timestamp(Flights_TimeStamp flights_timestamp) {
        this.flights_timestamp = flights_timestamp;
    }

}