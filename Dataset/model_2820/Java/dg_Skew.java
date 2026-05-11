





import java.util.List;
import java.util.ArrayList;

public class dg_Skew extends Transform {

    private String angleY;
    private String angleX;



    public dg_Skew(
        String angleY,        String angleX    ) {
        super(
        );
        this.angleY = angleY;
        this.angleX = angleX;
    }


    public String getAngley() {
        return angleY;
    }

    public void setAngley(String angleY) {
        this.angleY = angleY;
    }
    public String getAnglex() {
        return angleX;
    }

    public void setAnglex(String angleX) {
        this.angleX = angleX;
    }


}