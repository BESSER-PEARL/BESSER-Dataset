





import java.util.List;
import java.util.ArrayList;

public class Flights_Person extends FlightObject {

    private String travelState;





    private Flights_Persons flights_persons;


    public Flights_Person(
        String travelState    ) {
        super(
        );
        this.travelState = travelState;
    }


    public String getTravelstate() {
        return travelState;
    }

    public void setTravelstate(String travelState) {
        this.travelState = travelState;
    }

    public Flights_Persons getFlights_persons() {
        return flights_persons;
    }

    public void setFlights_persons(Flights_Persons flights_persons) {
        this.flights_persons = flights_persons;
    }

}