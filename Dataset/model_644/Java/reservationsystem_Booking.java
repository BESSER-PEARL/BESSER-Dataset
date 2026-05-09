





import java.util.List;
import java.util.ArrayList;

public class reservationsystem_Booking  {

    private String baggageInfo;
    private String bookNo;
    private int bookingStatus;





    private reservationsystem_SpecificFlight reservationsystem_specificflight;




    private reservationsystem_Passenger reservationsystem_passenger;




    private List<reservationsystem_SpecificFlight> reservationsystem_specificflights;




    private reservationsystem_Passenger reservationsystem_passenger;




    private List<reservationsystem_Passenger> reservationsystem_passengers;


    public reservationsystem_Booking(
        String baggageInfo,        String bookNo,        int bookingStatus    ) {
        this.baggageInfo = baggageInfo;
        this.bookNo = bookNo;
        this.bookingStatus = bookingStatus;
        this.reservationsystem_specificflights = new ArrayList<>();
        this.reservationsystem_passengers = new ArrayList<>();
    }

    public reservationsystem_Booking(
        String baggageInfo,        String bookNo,        int bookingStatus        ArrayList<reservationsystem_SpecificFlight> reservationsystem_specificflights,        ArrayList<reservationsystem_Passenger> reservationsystem_passengers    ) {
        this.baggageInfo = baggageInfo;
        this.bookNo = bookNo;
        this.bookingStatus = bookingStatus;
        this.reservationsystem_specificflights = reservationsystem_specificflights;
        this.reservationsystem_passengers = reservationsystem_passengers;
    }

    public String getBaggageinfo() {
        return baggageInfo;
    }

    public void setBaggageinfo(String baggageInfo) {
        this.baggageInfo = baggageInfo;
    }
    public String getBookno() {
        return bookNo;
    }

    public void setBookno(String bookNo) {
        this.bookNo = bookNo;
    }
    public int getBookingstatus() {
        return bookingStatus;
    }

    public void setBookingstatus(int bookingStatus) {
        this.bookingStatus = bookingStatus;
    }

    public reservationsystem_SpecificFlight getReservationsystem_specificflight() {
        return reservationsystem_specificflight;
    }

    public void setReservationsystem_specificflight(reservationsystem_SpecificFlight reservationsystem_specificflight) {
        this.reservationsystem_specificflight = reservationsystem_specificflight;
    }
    public reservationsystem_Passenger getReservationsystem_passenger() {
        return reservationsystem_passenger;
    }

    public void setReservationsystem_passenger(reservationsystem_Passenger reservationsystem_passenger) {
        this.reservationsystem_passenger = reservationsystem_passenger;
    }
    public List<reservationsystem_SpecificFlight> getReservationsystem_specificflights() {
        return reservationsystem_specificflights;
    }

    public void addReservationsystem_specificflight(Reservationsystem_specificflight reservationsystem_specificflight) {
        this.reservationsystem_specificflights.add(reservationsystem_specificflight);
    }
    public reservationsystem_Passenger getReservationsystem_passenger() {
        return reservationsystem_passenger;
    }

    public void setReservationsystem_passenger(reservationsystem_Passenger reservationsystem_passenger) {
        this.reservationsystem_passenger = reservationsystem_passenger;
    }
    public List<reservationsystem_Passenger> getReservationsystem_passengers() {
        return reservationsystem_passengers;
    }

    public void addReservationsystem_passenger(Reservationsystem_passenger reservationsystem_passenger) {
        this.reservationsystem_passengers.add(reservationsystem_passenger);
    }

}