





import java.util.List;
import java.util.ArrayList;

public class mMDSL_PathParametersC  {

    private String y1;
    private String y2;
    private String y;
    private String x2;
    private String x1;
    private String x;





    private mMDSL_CurveTo mmdsl_curveto;


    public mMDSL_PathParametersC(
        String y1,        String y2,        String y,        String x2,        String x1,        String x    ) {
        this.y1 = y1;
        this.y2 = y2;
        this.y = y;
        this.x2 = x2;
        this.x1 = x1;
        this.x = x;
    }


    public String getY1() {
        return y1;
    }

    public void setY1(String y1) {
        this.y1 = y1;
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
    public String getX2() {
        return x2;
    }

    public void setX2(String x2) {
        this.x2 = x2;
    }
    public String getX1() {
        return x1;
    }

    public void setX1(String x1) {
        this.x1 = x1;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    public mMDSL_CurveTo getMmdsl_curveto() {
        return mmdsl_curveto;
    }

    public void setMmdsl_curveto(mMDSL_CurveTo mmdsl_curveto) {
        this.mmdsl_curveto = mmdsl_curveto;
    }

}