





import java.util.List;
import java.util.ArrayList;

public class First_Class  {

    private String First_Seat_Price;
    private String First_Seat_ID;



    public First_Class(
        String First_Seat_Price,        String First_Seat_ID    ) {
        this.First_Seat_Price = First_Seat_Price;
        this.First_Seat_ID = First_Seat_ID;
    }


    public String getFirst_seat_price() {
        return First_Seat_Price;
    }

    public void setFirst_seat_price(String First_Seat_Price) {
        this.First_Seat_Price = First_Seat_Price;
    }
    public String getFirst_seat_id() {
        return First_Seat_ID;
    }

    public void setFirst_seat_id(String First_Seat_ID) {
        this.First_Seat_ID = First_Seat_ID;
    }


}