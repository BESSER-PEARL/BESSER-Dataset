





import java.util.List;
import java.util.ArrayList;

public class CodePack_DataModels_Guest  {

    private String name;
    private int booking_id;



    public CodePack_DataModels_Guest(
        String name,        int booking_id    ) {
        this.name = name;
        this.booking_id = booking_id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(int booking_id) {
        this.booking_id = booking_id;
    }


}