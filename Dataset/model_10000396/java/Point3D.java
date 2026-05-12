





import java.util.List;
import java.util.ArrayList;

public class Point3D  {

    private int Y;
    private int X;
    private int Z;



    public Point3D(
        int Y,        int X,        int Z    ) {
        this.Y = Y;
        this.X = X;
        this.Z = Z;
    }


    public int getY() {
        return Y;
    }

    public void setY(int Y) {
        this.Y = Y;
    }
    public int getX() {
        return X;
    }

    public void setX(int X) {
        this.X = X;
    }
    public int getZ() {
        return Z;
    }

    public void setZ(int Z) {
        this.Z = Z;
    }


}