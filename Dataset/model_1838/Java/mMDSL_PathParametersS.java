





import java.util.List;
import java.util.ArrayList;

public class mMDSL_PathParametersS  {

    private String y2;
    private String y;
    private String x;
    private String x2;





    private mMDSL_SmoothCurveTo mmdsl_smoothcurveto;


    public mMDSL_PathParametersS(
        String y2,        String y,        String x,        String x2    ) {
        this.y2 = y2;
        this.y = y;
        this.x = x;
        this.x2 = x2;
    }


    public String getY2() {
        return y2;
    }

    public void setY2(String y2) {
        this.y2 = y2;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getX2() {
        return x2;
    }

    public void setX2(String x2) {
        this.x2 = x2;
    }

    public mMDSL_SmoothCurveTo getMmdsl_smoothcurveto() {
        return mmdsl_smoothcurveto;
    }

    public void setMmdsl_smoothcurveto(mMDSL_SmoothCurveTo mmdsl_smoothcurveto) {
        this.mmdsl_smoothcurveto = mmdsl_smoothcurveto;
    }

}