





import java.util.List;
import java.util.ArrayList;

public class mMDSL_PathParametersA  {

    private String x;
    private String sweepflag;
    private String rx;
    private String ry;
    private String largearcflag;
    private String y;
    private String xaxisrot;





    private mMDSL_EllipticalArc mmdsl_ellipticalarc;


    public mMDSL_PathParametersA(
        String x,        String sweepflag,        String rx,        String ry,        String largearcflag,        String y,        String xaxisrot    ) {
        this.x = x;
        this.sweepflag = sweepflag;
        this.rx = rx;
        this.ry = ry;
        this.largearcflag = largearcflag;
        this.y = y;
        this.xaxisrot = xaxisrot;
    }


    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getSweepflag() {
        return sweepflag;
    }

    public void setSweepflag(String sweepflag) {
        this.sweepflag = sweepflag;
    }
    public String getRx() {
        return rx;
    }

    public void setRx(String rx) {
        this.rx = rx;
    }
    public String getRy() {
        return ry;
    }

    public void setRy(String ry) {
        this.ry = ry;
    }
    public String getLargearcflag() {
        return largearcflag;
    }

    public void setLargearcflag(String largearcflag) {
        this.largearcflag = largearcflag;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getXaxisrot() {
        return xaxisrot;
    }

    public void setXaxisrot(String xaxisrot) {
        this.xaxisrot = xaxisrot;
    }

    public mMDSL_EllipticalArc getMmdsl_ellipticalarc() {
        return mmdsl_ellipticalarc;
    }

    public void setMmdsl_ellipticalarc(mMDSL_EllipticalArc mmdsl_ellipticalarc) {
        this.mmdsl_ellipticalarc = mmdsl_ellipticalarc;
    }

}