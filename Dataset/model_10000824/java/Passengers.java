





import java.util.List;
import java.util.ArrayList;

public class Passengers  {

    private String passenger_name;
    private String Passenger_TKT_No;
    private String Passenger_Details;





    private Qaboos_Airways qaboos_airways;


    public Passengers(
        String passenger_name,        String Passenger_TKT_No,        String Passenger_Details    ) {
        this.passenger_name = passenger_name;
        this.Passenger_TKT_No = Passenger_TKT_No;
        this.Passenger_Details = Passenger_Details;
    }


    public String getPassenger_name() {
        return passenger_name;
    }

    public void setPassenger_name(String passenger_name) {
        this.passenger_name = passenger_name;
    }
    public String getPassenger_tkt_no() {
        return Passenger_TKT_No;
    }

    public void setPassenger_tkt_no(String Passenger_TKT_No) {
        this.Passenger_TKT_No = Passenger_TKT_No;
    }
    public String getPassenger_details() {
        return Passenger_Details;
    }

    public void setPassenger_details(String Passenger_Details) {
        this.Passenger_Details = Passenger_Details;
    }

    public Qaboos_Airways getQaboos_airways() {
        return qaboos_airways;
    }

    public void setQaboos_airways(Qaboos_Airways qaboos_airways) {
        this.qaboos_airways = qaboos_airways;
    }

}