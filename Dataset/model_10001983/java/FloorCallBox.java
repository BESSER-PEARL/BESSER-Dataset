





import java.util.List;
import java.util.ArrayList;

public class FloorCallBox  {

    private int LOCATION;
    private None BUTTONS;





    private Floor floor;


    public FloorCallBox(
        int LOCATION,        None BUTTONS    ) {
        this.LOCATION = LOCATION;
        this.BUTTONS = BUTTONS;
    }


    public int getLocation() {
        return LOCATION;
    }

    public void setLocation(int LOCATION) {
        this.LOCATION = LOCATION;
    }
    public None getButtons() {
        return BUTTONS;
    }

    public void setButtons(None BUTTONS) {
        this.BUTTONS = BUTTONS;
    }

    public Floor getFloor() {
        return floor;
    }

    public void setFloor(Floor floor) {
        this.floor = floor;
    }

}