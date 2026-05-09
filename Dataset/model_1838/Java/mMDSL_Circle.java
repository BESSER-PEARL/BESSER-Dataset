





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Circle  {

    private String cy;
    private String r;
    private String cx;





    private mMDSL_SVGCommand mmdsl_svgcommand;


    public mMDSL_Circle(
        String cy,        String r,        String cx    ) {
        this.cy = cy;
        this.r = r;
        this.cx = cx;
    }


    public String getCy() {
        return cy;
    }

    public void setCy(String cy) {
        this.cy = cy;
    }
    public String getR() {
        return r;
    }

    public void setR(String r) {
        this.r = r;
    }
    public String getCx() {
        return cx;
    }

    public void setCx(String cx) {
        this.cx = cx;
    }

    public mMDSL_SVGCommand getMmdsl_svgcommand() {
        return mmdsl_svgcommand;
    }

    public void setMmdsl_svgcommand(mMDSL_SVGCommand mmdsl_svgcommand) {
        this.mmdsl_svgcommand = mmdsl_svgcommand;
    }

}