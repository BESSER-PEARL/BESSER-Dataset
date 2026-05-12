





import java.util.List;
import java.util.ArrayList;

public class Flight  {

    private String Flgt_NO;
    private String Flgt_Details;





    private Qaboos_Airways qaboos_airways;




    private Passengers passengers;


    public Flight(
        String Flgt_NO,        String Flgt_Details    ) {
        this.Flgt_NO = Flgt_NO;
        this.Flgt_Details = Flgt_Details;
    }


    public String getFlgt_no() {
        return Flgt_NO;
    }

    public void setFlgt_no(String Flgt_NO) {
        this.Flgt_NO = Flgt_NO;
    }
    public String getFlgt_details() {
        return Flgt_Details;
    }

    public void setFlgt_details(String Flgt_Details) {
        this.Flgt_Details = Flgt_Details;
    }

    public Qaboos_Airways getQaboos_airways() {
        return qaboos_airways;
    }

    public void setQaboos_airways(Qaboos_Airways qaboos_airways) {
        this.qaboos_airways = qaboos_airways;
    }
    public Passengers getPassengers() {
        return passengers;
    }

    public void setPassengers(Passengers passengers) {
        this.passengers = passengers;
    }

}