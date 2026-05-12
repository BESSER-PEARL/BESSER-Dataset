





import java.util.List;
import java.util.ArrayList;

public class Infant  {

    private String Infant_Seat_Price;
    private String Infant_No;



    public Infant(
        String Infant_Seat_Price,        String Infant_No    ) {
        this.Infant_Seat_Price = Infant_Seat_Price;
        this.Infant_No = Infant_No;
    }


    public String getInfant_seat_price() {
        return Infant_Seat_Price;
    }

    public void setInfant_seat_price(String Infant_Seat_Price) {
        this.Infant_Seat_Price = Infant_Seat_Price;
    }
    public String getInfant_no() {
        return Infant_No;
    }

    public void setInfant_no(String Infant_No) {
        this.Infant_No = Infant_No;
    }


}