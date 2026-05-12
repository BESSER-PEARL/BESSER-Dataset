





import java.util.List;
import java.util.ArrayList;

public class Flight  {

    private String Date;
    private String FlightNumber;



    public Flight(
        String Date,        String FlightNumber    ) {
        this.Date = Date;
        this.FlightNumber = FlightNumber;
    }


    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getFlightnumber() {
        return FlightNumber;
    }

    public void setFlightnumber(String FlightNumber) {
        this.FlightNumber = FlightNumber;
    }


}