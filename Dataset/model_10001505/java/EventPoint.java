





import java.util.List;
import java.util.ArrayList;

public class EventPoint  {

    private int type;
    private None location;
    private String time;



    public EventPoint(
        int type,        None location,        String time    ) {
        this.type = type;
        this.location = location;
        this.time = time;
    }


    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public None getLocation() {
        return location;
    }

    public void setLocation(None location) {
        this.location = location;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }


}