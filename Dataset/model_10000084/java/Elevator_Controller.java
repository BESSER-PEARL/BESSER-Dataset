





import java.util.List;
import java.util.ArrayList;

public class Elevator_Controller  {

    private String attribute;
    private boolean Direction;
    private int Floor_ID;
    private int Position;



    public Elevator_Controller(
        String attribute,        boolean Direction,        int Floor_ID,        int Position    ) {
        this.attribute = attribute;
        this.Direction = Direction;
        this.Floor_ID = Floor_ID;
        this.Position = Position;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public boolean getDirection() {
        return Direction;
    }

    public void setDirection(boolean Direction) {
        this.Direction = Direction;
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


}