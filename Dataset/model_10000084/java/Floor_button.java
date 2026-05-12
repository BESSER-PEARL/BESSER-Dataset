





import java.util.List;
import java.util.ArrayList;

public class Floor_button  {

    private int Floor_num;
    private boolean Direction;



    public Floor_button(
        int Floor_num,        boolean Direction    ) {
        this.Floor_num = Floor_num;
        this.Direction = Direction;
    }


    public int getFloor_num() {
        return Floor_num;
    }

    public void setFloor_num(int Floor_num) {
        this.Floor_num = Floor_num;
    }
    public boolean getDirection() {
        return Direction;
    }

    public void setDirection(boolean Direction) {
        this.Direction = Direction;
    }


}