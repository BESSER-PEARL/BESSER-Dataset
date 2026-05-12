





import java.util.List;
import java.util.ArrayList;

public class Economy_Seats  {

    private String Eco_Seat_Price;
    private String Eco_Seat_ID;



    public Economy_Seats(
        String Eco_Seat_Price,        String Eco_Seat_ID    ) {
        this.Eco_Seat_Price = Eco_Seat_Price;
        this.Eco_Seat_ID = Eco_Seat_ID;
    }


    public String getEco_seat_price() {
        return Eco_Seat_Price;
    }

    public void setEco_seat_price(String Eco_Seat_Price) {
        this.Eco_Seat_Price = Eco_Seat_Price;
    }
    public String getEco_seat_id() {
        return Eco_Seat_ID;
    }

    public void setEco_seat_id(String Eco_Seat_ID) {
        this.Eco_Seat_ID = Eco_Seat_ID;
    }


}