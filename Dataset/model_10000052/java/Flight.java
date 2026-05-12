




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Flight  {

    private int id;
    private LocalDate departureTime;
    private LocalDate arrivalTime;





    private Airline airline;


    public Flight(
        int id,        LocalDate departureTime,        LocalDate arrivalTime    ) {
        this.id = id;
        this.departureTime = departureTime;
        this.arrivalTime = arrivalTime;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getDeparturetime() {
        return departureTime;
    }

    public void setDeparturetime(LocalDate departureTime) {
        this.departureTime = departureTime;
    }
    public LocalDate getArrivaltime() {
        return arrivalTime;
    }

    public void setArrivaltime(LocalDate arrivalTime) {
        this.arrivalTime = arrivalTime;
    }

    public Airline getAirline() {
        return airline;
    }

    public void setAirline(Airline airline) {
        this.airline = airline;
    }

}