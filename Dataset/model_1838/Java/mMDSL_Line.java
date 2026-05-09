





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Line  {

    private String x2;
    private String y2;
    private String y1;
    private String x1;





    private mMDSL_SVGCommand mmdsl_svgcommand;


    public mMDSL_Line(
        String x2,        String y2,        String y1,        String x1    ) {
        this.x2 = x2;
        this.y2 = y2;
        this.y1 = y1;
        this.x1 = x1;
    }


    public String getX2() {
        return x2;
    }

    public void setX2(String x2) {
        this.x2 = x2;
    }
    public String getY2() {
        return y2;
    }

    public void setY2(String y2) {
        this.y2 = y2;
    }
    public String getY1() {
        return y1;
    }

    public void setY1(String y1) {
        this.y1 = y1;
    }
    public String getX1() {
        return x1;
    }

    public void setX1(String x1) {
        this.x1 = x1;
    }

    public mMDSL_SVGCommand getMmdsl_svgcommand() {
        return mmdsl_svgcommand;
    }

    public void setMmdsl_svgcommand(mMDSL_SVGCommand mmdsl_svgcommand) {
        this.mmdsl_svgcommand = mmdsl_svgcommand;
    }

}