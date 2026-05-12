





import java.util.List;
import java.util.ArrayList;

public class Parking_Space  {

    private None Space_Type;
    private None Floor_Number;
    private int Space_Number;



    public Parking_Space(
        None Space_Type,        None Floor_Number,        int Space_Number    ) {
        this.Space_Type = Space_Type;
        this.Floor_Number = Floor_Number;
        this.Space_Number = Space_Number;
    }


    public None getSpace_type() {
        return Space_Type;
    }

    public void setSpace_type(None Space_Type) {
        this.Space_Type = Space_Type;
    }
    public None getFloor_number() {
        return Floor_Number;
    }

    public void setFloor_number(None Floor_Number) {
        this.Floor_Number = Floor_Number;
    }
    public int getSpace_number() {
        return Space_Number;
    }

    public void setSpace_number(int Space_Number) {
        this.Space_Number = Space_Number;
    }


}