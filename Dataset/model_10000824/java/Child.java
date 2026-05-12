





import java.util.List;
import java.util.ArrayList;

public class Child  {

    private String Child_Seat_Price;
    private String Child_ID;



    public Child(
        String Child_Seat_Price,        String Child_ID    ) {
        this.Child_Seat_Price = Child_Seat_Price;
        this.Child_ID = Child_ID;
    }


    public String getChild_seat_price() {
        return Child_Seat_Price;
    }

    public void setChild_seat_price(String Child_Seat_Price) {
        this.Child_Seat_Price = Child_Seat_Price;
    }
    public String getChild_id() {
        return Child_ID;
    }

    public void setChild_id(String Child_ID) {
        this.Child_ID = Child_ID;
    }


}