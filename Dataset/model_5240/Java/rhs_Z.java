





import java.util.List;
import java.util.ArrayList;

public class rhs_Z  {

    private String z;





    private rhs_X rhs_x;




    private List<rhs_Y> rhs_ys;


    public rhs_Z(
        String z    ) {
        this.z = z;
        this.rhs_ys = new ArrayList<>();
    }

    public rhs_Z(
        String z        ArrayList<rhs_Y> rhs_ys    ) {
        this.z = z;
        this.rhs_ys = rhs_ys;
    }

    public String getZ() {
        return z;
    }

    public void setZ(String z) {
        this.z = z;
    }

    public rhs_X getRhs_x() {
        return rhs_x;
    }

    public void setRhs_x(rhs_X rhs_x) {
        this.rhs_x = rhs_x;
    }
    public List<rhs_Y> getRhs_ys() {
        return rhs_ys;
    }

    public void addRhs_y(Rhs_y rhs_y) {
        this.rhs_ys.add(rhs_y);
    }

}