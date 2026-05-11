





import java.util.List;
import java.util.ArrayList;

public class dg_Rotate extends Transform {

    private String angle;





    private dg_Point dg_point;


    public dg_Rotate(
        String angle    ) {
        super(
        );
        this.angle = angle;
    }


    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }

    public dg_Point getDg_point() {
        return dg_point;
    }

    public void setDg_point(dg_Point dg_point) {
        this.dg_point = dg_point;
    }

}