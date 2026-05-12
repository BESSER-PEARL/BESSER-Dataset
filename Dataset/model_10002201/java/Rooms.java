





import java.util.List;
import java.util.ArrayList;

public class Rooms  {

    private String Location;
    private int Roomno_;



    public Rooms(
        String Location,        int Roomno_    ) {
        this.Location = Location;
        this.Roomno_ = Roomno_;
    }


    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }
    public int getRoomno_() {
        return Roomno_;
    }

    public void setRoomno_(int Roomno_) {
        this.Roomno_ = Roomno_;
    }


}