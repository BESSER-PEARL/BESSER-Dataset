





import java.util.List;
import java.util.ArrayList;

public class HALL_Geometry_Point3D extends Point {

    private int zCoord;





    private Face face;


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

    public Face getFace() {
        return face;
    }

    public void setFace(Face face) {
        this.face = face;
    }

}