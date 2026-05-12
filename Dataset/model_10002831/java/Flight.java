




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Flight  {

    private LocalDate arrivalTime;
    private LocalDate departureTime;
    private int id;





    private Airline airline;




    private Aircraft aircraft;


    public Flight(
        LocalDate arrivalTime,        LocalDate departureTime,        int id    ) {
        this.arrivalTime = arrivalTime;
        this.departureTime = departureTime;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Airline getAirline() {
        return airline;
    }

    public void setAirline(Airline airline) {
        this.airline = airline;
    }
    public Aircraft getAircraft() {
        return aircraft;
    }

    public void setAircraft(Aircraft aircraft) {
        this.aircraft = aircraft;
    }

}