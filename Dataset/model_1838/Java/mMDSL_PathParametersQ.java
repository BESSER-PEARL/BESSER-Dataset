





import java.util.List;
import java.util.ArrayList;

public class mMDSL_PathParametersQ  {

    private String y1;
    private String y;
    private String x1;
    private String x;





    private mMDSL_QuadraticBezierCurve mmdsl_quadraticbeziercurve;


    public mMDSL_PathParametersQ(
        String y1,        String y,        String x1,        String x    ) {
        this.y1 = y1;
        this.y = y;
        this.x1 = x1;
        this.x = x;
    }


    public String getY1() {
        return y1;
    }

    public void setY1(String y1) {
        this.y1 = y1;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
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

    public mMDSL_QuadraticBezierCurve getMmdsl_quadraticbeziercurve() {
        return mmdsl_quadraticbeziercurve;
    }

    public void setMmdsl_quadraticbeziercurve(mMDSL_QuadraticBezierCurve mmdsl_quadraticbeziercurve) {
        this.mmdsl_quadraticbeziercurve = mmdsl_quadraticbeziercurve;
    }

}