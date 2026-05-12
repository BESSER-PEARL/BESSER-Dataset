





import java.util.List;
import java.util.ArrayList;

public class Elevator_Controller_2  {

    private String attribute;
    private int Floor_ID;
    private int Position;
    private boolean Direction;



    public Elevator_Controller_2(
        String attribute,        int Floor_ID,        int Position,        boolean Direction    ) {
        this.attribute = attribute;
        this.Floor_ID = Floor_ID;
        this.Position = Position;
        this.Direction = Direction;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getFloor_id() {
        return Floor_ID;
    }

    public void setFloor_id(int Floor_ID) {
        this.Floor_ID = Floor_ID;
    }
    public int getPosition() {
        return Position;
    }

    public void setPosition(int Position) {
        this.Position = Position;
    }
    public boolean getDirection() {
        return Direction;
    }

    public void setDirection(boolean Direction) {
        this.Direction = Direction;
    }


}