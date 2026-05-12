




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Flight  {

    private int id;
    private LocalDate arrivalTime;
    private LocalDate departureTime;





    private Airline airline;


    public Flight(
        int id,        LocalDate arrivalTime,        LocalDate departureTime    ) {
        this.id = id;
        this.arrivalTime = arrivalTime;
        this.departureTime = departureTime;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getArrivaltime() {
        return arrivalTime;
    }

    public void setArrivaltime(LocalDate arrivalTime) {
        this.arrivalTime = arrivalTime;
    }
    public LocalDate getDeparturetime() {
        return departureTime;
    }

    public void setDeparturetime(LocalDate departureTime) {
        this.departureTime = departureTime;
    }

    public Airline getAirline() {
        return airline;
    }

    public void setAirline(Airline airline) {
        this.airline = airline;
    }

}