





import java.util.List;
import java.util.ArrayList;

public class mMDSL_Text  {

    private String value;
    private String fontsize;
    private String x;
    private String y;





    private mMDSL_SVGCommand mmdsl_svgcommand;


    public mMDSL_Text(
        String value,        String fontsize,        String x,        String y    ) {
        this.value = value;
        this.fontsize = fontsize;
        this.x = x;
        this.y = y;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getFontsize() {
        return fontsize;
    }

    public void setFontsize(String fontsize) {
        this.fontsize = fontsize;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }

    public mMDSL_SVGCommand getMmdsl_svgcommand() {
        return mmdsl_svgcommand;
    }

    public void setMmdsl_svgcommand(mMDSL_SVGCommand mmdsl_svgcommand) {
        this.mmdsl_svgcommand = mmdsl_svgcommand;
    }

}