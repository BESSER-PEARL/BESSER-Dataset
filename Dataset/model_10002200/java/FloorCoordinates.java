





import java.util.List;
import java.util.ArrayList;

public class FloorCoordinates  {

    private int YcoordinatePosition;
    private int XcoordinatePosition;



    public FloorCoordinates(
        int YcoordinatePosition,        int XcoordinatePosition    ) {
        this.YcoordinatePosition = YcoordinatePosition;
        this.XcoordinatePosition = XcoordinatePosition;
    }


    public int getYcoordinateposition() {
        return YcoordinatePosition;
    }

    public void setYcoordinateposition(int YcoordinatePosition) {
        this.YcoordinatePosition = YcoordinatePosition;
    }
    public int getXcoordinateposition() {
        return XcoordinatePosition;
    }

    public void setXcoordinateposition(int XcoordinatePosition) {
        this.XcoordinatePosition = XcoordinatePosition;
    }


}