





import java.util.List;
import java.util.ArrayList;

public class Adult  {

    private String Adult_Seat_Price;
    private String Adult_ID;



    public Adult(
        String Adult_Seat_Price,        String Adult_ID    ) {
        this.Adult_Seat_Price = Adult_Seat_Price;
        this.Adult_ID = Adult_ID;
    }


    public String getAdult_seat_price() {
        return Adult_Seat_Price;
    }

    public void setAdult_seat_price(String Adult_Seat_Price) {
        this.Adult_Seat_Price = Adult_Seat_Price;
    }
    public String getAdult_id() {
        return Adult_ID;
    }

    public void setAdult_id(String Adult_ID) {
        this.Adult_ID = Adult_ID;
    }


}