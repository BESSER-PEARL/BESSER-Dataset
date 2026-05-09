





import java.util.List;
import java.util.ArrayList;

public class HALL_Geometry_Point3D extends Point {

    private int zCoord;



    public HALL_Geometry_Point3D(
        int zCoord    ) {
        super(
        );
        this.zCoord = zCoord;
    }


    public int getZcoord() {
        return zCoord;
    }

    public void setZcoord(int zCoord) {
        this.zCoord = zCoord;
    }


}