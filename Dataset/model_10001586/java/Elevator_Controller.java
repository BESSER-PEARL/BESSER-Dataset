





import java.util.List;
import java.util.ArrayList;

public class Elevator_Controller  {

    private String attribute;
    private int Position;
    private boolean Direction;
    private int Floor_ID;



    public Elevator_Controller(
        String attribute,        int Position,        boolean Direction,        int Floor_ID    ) {
        this.attribute = attribute;
        this.Position = Position;
        this.Direction = Direction;
        this.Floor_ID = Floor_ID;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
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
    public int getFloor_id() {
        return Floor_ID;
    }

    public void setFloor_id(int Floor_ID) {
        this.Floor_ID = Floor_ID;
    }


}