





import java.util.List;
import java.util.ArrayList;

public class xyz_Y  {






    private List<xyz_Z> xyz_zs;




    private xyz_X xyz_x;


    public xyz_Y(
    ) {
        this.xyz_zs = new ArrayList<>();
    }

    public xyz_Y(
        ArrayList<xyz_Z> xyz_zs    ) {
        this.xyz_zs = xyz_zs;
    }


    public List<xyz_Z> getXyz_zs() {
        return xyz_zs;
    }

    public void addXyz_z(Xyz_z xyz_z) {
        this.xyz_zs.add(xyz_z);
    }
    public xyz_X getXyz_x() {
        return xyz_x;
    }

    public void setXyz_x(xyz_X xyz_x) {
        this.xyz_x = xyz_x;
    }

}