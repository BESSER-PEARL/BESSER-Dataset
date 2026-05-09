





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Rectangle  {

    private String y;
    private String height;
    private String x;
    private String width;





    private mMDSL_SVGCommand mmdsl_svgcommand;


    public mMDSL_Rectangle(
        String y,        String height,        String x,        String width    ) {
        this.y = y;
        this.height = height;
        this.x = x;
        this.width = width;
    }


    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }

    public mMDSL_SVGCommand getMmdsl_svgcommand() {
        return mmdsl_svgcommand;
    }

    public void setMmdsl_svgcommand(mMDSL_SVGCommand mmdsl_svgcommand) {
        this.mmdsl_svgcommand = mmdsl_svgcommand;
    }

}