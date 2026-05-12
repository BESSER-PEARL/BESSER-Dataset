





import java.util.List;
import java.util.ArrayList;

public class Floor_button  {

    private boolean Direction;
    private int Floor_num;



    public Floor_button(
        boolean Direction,        int Floor_num    ) {
        this.Direction = Direction;
        this.Floor_num = Floor_num;
    }


    public boolean getDirection() {
        return Direction;
    }

    public void setDirection(boolean Direction) {
        this.Direction = Direction;
    }
    public int getFloor_num() {
        return Floor_num;
    }

    public void setFloor_num(int Floor_num) {
        this.Floor_num = Floor_num;
    }


}