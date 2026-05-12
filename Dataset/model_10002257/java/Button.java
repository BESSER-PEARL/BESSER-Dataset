





import java.util.List;
import java.util.ArrayList;

public class Button  {

    private boolean pressed;
    private int floor;



    public Button(
        boolean pressed,        int floor    ) {
        this.pressed = pressed;
        this.floor = floor;
    }


    public boolean getPressed() {
        return pressed;
    }

    public void setPressed(boolean pressed) {
        this.pressed = pressed;
    }
    public int getFloor() {
        return floor;
    }

    public void setFloor(int floor) {
        this.floor = floor;
    }


}