





import java.util.List;
import java.util.ArrayList;

public class reservationsystem_GeneralFlight  {

    private String departureTime;
    private String arrivalTime;
    private String flightNo;





    private List<reservationsystem_SpecificFlight> reservationsystem_specificflights;




    private reservationsystem_SpecificFlight reservationsystem_specificflight;


    public reservationsystem_GeneralFlight(
        String departureTime,        String arrivalTime,        String flightNo    ) {
        this.departureTime = departureTime;
        this.arrivalTime = arrivalTime;
        this.flightNo = flightNo;
        this.reservationsystem_specificflights = new ArrayList<>();
    }

    public reservationsystem_GeneralFlight(
        String departureTime,        String arrivalTime,        String flightNo        ArrayList<reservationsystem_SpecificFlight> reservationsystem_specificflights    ) {
        this.departureTime = departureTime;
        this.arrivalTime = arrivalTime;
        this.flightNo = flightNo;
        this.reservationsystem_specificflights = reservationsystem_specificflights;
    }

    public String getDeparturetime() {
        return departureTime;
    }

    public void setDeparturetime(String departureTime) {
        this.departureTime = departureTime;
    }
    public String getArrivaltime() {
        return arrivalTime;
    }

    public void setArrivaltime(String arrivalTime) {
        this.arrivalTime = arrivalTime;
    }
    public String getFlightno() {
        return flightNo;
    }

    public void setFlightno(String flightNo) {
        this.flightNo = flightNo;
    }

    public List<reservationsystem_SpecificFlight> getReservationsystem_specificflights() {
        return reservationsystem_specificflights;
    }

    public void addReservationsystem_specificflight(Reservationsystem_specificflight reservationsystem_specificflight) {
        this.reservationsystem_specificflights.add(reservationsystem_specificflight);
    }
    public reservationsystem_SpecificFlight getReservationsystem_specificflight() {
        return reservationsystem_specificflight;
    }

    public void setReservationsystem_specificflight(reservationsystem_SpecificFlight reservationsystem_specificflight) {
        this.reservationsystem_specificflight = reservationsystem_specificflight;
    }

}