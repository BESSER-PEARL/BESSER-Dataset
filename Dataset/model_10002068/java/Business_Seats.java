





import java.util.List;
import java.util.ArrayList;

public class Business_Seats  {

    private String Buiss_Seat_Price;
    private String Buiss_Seat_ID;



    public Business_Seats(
        String Buiss_Seat_Price,        String Buiss_Seat_ID    ) {
        this.Buiss_Seat_Price = Buiss_Seat_Price;
        this.Buiss_Seat_ID = Buiss_Seat_ID;
    }


    public String getBuiss_seat_price() {
        return Buiss_Seat_Price;
    }

    public void setBuiss_seat_price(String Buiss_Seat_Price) {
        this.Buiss_Seat_Price = Buiss_Seat_Price;
    }
    public String getBuiss_seat_id() {
        return Buiss_Seat_ID;
    }

    public void setBuiss_seat_id(String Buiss_Seat_ID) {
        this.Buiss_Seat_ID = Buiss_Seat_ID;
    }


}