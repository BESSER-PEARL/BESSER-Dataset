





import java.util.List;
import java.util.ArrayList;

public class Flight  {

    private String FlightNumber;
    private String Date;



    public Flight(
        String FlightNumber,        String Date    ) {
        this.FlightNumber = FlightNumber;
        this.Date = Date;
    }


    public String getFlightnumber() {
        return FlightNumber;
    }

    public void setFlightnumber(String FlightNumber) {
        this.FlightNumber = FlightNumber;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }


}