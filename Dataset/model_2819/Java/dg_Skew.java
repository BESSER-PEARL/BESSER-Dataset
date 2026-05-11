





import java.util.List;
import java.util.ArrayList;

public class dg_Skew extends Transform {

    private String angleX;
    private String angleY;



    public dg_Skew(
        String angleX,        String angleY    ) {
        super(
        );
        this.angleX = angleX;
        this.angleY = angleY;
    }


    public String getAnglex() {
        return angleX;
    }

    public void setAnglex(String angleX) {
        this.angleX = angleX;
    }
    public String getAngley() {
        return angleY;
    }

    public void setAngley(String angleY) {
        this.angleY = angleY;
    }


}