





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Ellipse  {

    private String ry;
    private String rx;
    private String cy;
    private String cx;





    private mMDSL_SVGCommand mmdsl_svgcommand;


    public mMDSL_Ellipse(
        String ry,        String rx,        String cy,        String cx    ) {
        this.ry = ry;
        this.rx = rx;
        this.cy = cy;
        this.cx = cx;
    }


    public String getRy() {
        return ry;
    }

    public void setRy(String ry) {
        this.ry = ry;
    }
    public String getRx() {
        return rx;
    }

    public void setRx(String rx) {
        this.rx = rx;
    }
    public String getCy() {
        return cy;
    }

    public void setCy(String cy) {
        this.cy = cy;
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