





import java.util.List;
import java.util.ArrayList;

public class FLIGHT  {

    private int Flight_No_;
    private String Flight_Name;



    public FLIGHT(
        int Flight_No_,        String Flight_Name    ) {
        this.Flight_No_ = Flight_No_;
        this.Flight_Name = Flight_Name;
    }


    public int getFlight_no_() {
        return Flight_No_;
    }

    public void setFlight_no_(int Flight_No_) {
        this.Flight_No_ = Flight_No_;
    }
    public String getFlight_name() {
        return Flight_Name;
    }

    public void setFlight_name(String Flight_Name) {
        this.Flight_Name = Flight_Name;
    }


}