




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class trip_model_Trip  {

    private LocalDate End;
    private String name;
    private LocalDate Start;





    private trip_model_location trip_model_location;




    private trip_model_location trip_model_location;




    private List<trip_model_Service> trip_model_services;


    public trip_model_Trip(
        LocalDate End,        String name,        LocalDate Start    ) {
        this.End = End;
        this.name = name;
        this.Start = Start;
        this.trip_model_services = new ArrayList<>();
    }

    public trip_model_Trip(
        LocalDate End,        String name,        LocalDate Start        ArrayList<trip_model_Service> trip_model_services    ) {
        this.End = End;
        this.name = name;
        this.Start = Start;
        this.trip_model_services = trip_model_services;
    }

    public LocalDate getEnd() {
        return End;
    }

    public void setEnd(LocalDate End) {
        this.End = End;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getStart() {
        return Start;
    }

    public void setStart(LocalDate Start) {
        this.Start = Start;
    }

    public trip_model_location getTrip_model_location() {
        return trip_model_location;
    }

    public void setTrip_model_location(trip_model_location trip_model_location) {
        this.trip_model_location = trip_model_location;
    }
    public trip_model_location getTrip_model_location() {
        return trip_model_location;
    }

    public void setTrip_model_location(trip_model_location trip_model_location) {
        this.trip_model_location = trip_model_location;
    }
    public List<trip_model_Service> getTrip_model_services() {
        return trip_model_services;
    }

    public void addTrip_model_service(Trip_model_service trip_model_service) {
        this.trip_model_services.add(trip_model_service);
    }

}