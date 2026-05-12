





import java.util.List;
import java.util.ArrayList;

public class Parking_Space  {

    private boolean Occupied;
    private None Space_Type;
    private int Space_Number;
    private None Floor_Number;



    public Parking_Space(
        boolean Occupied,        None Space_Type,        int Space_Number,        None Floor_Number    ) {
        this.Occupied = Occupied;
        this.Space_Type = Space_Type;
        this.Space_Number = Space_Number;
        this.Floor_Number = Floor_Number;
    }


    public boolean getOccupied() {
        return Occupied;
    }

    public void setOccupied(boolean Occupied) {
        this.Occupied = Occupied;
    }
    public None getSpace_type() {
        return Space_Type;
    }

    public void setSpace_type(None Space_Type) {
        this.Space_Type = Space_Type;
    }
    public int getSpace_number() {
        return Space_Number;
    }

    public void setSpace_number(int Space_Number) {
        this.Space_Number = Space_Number;
    }
    public None getFloor_number() {
        return Floor_Number;
    }

    public void setFloor_number(None Floor_Number) {
        this.Floor_Number = Floor_Number;
    }


}