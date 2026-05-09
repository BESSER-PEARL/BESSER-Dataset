





import java.util.List;
import java.util.ArrayList;

public class tda593_booking_RoomStay  {

    private int id;
    private boolean active;



    public tda593_booking_RoomStay(
        int id,        boolean active    ) {
        this.id = id;
        this.active = active;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }


}