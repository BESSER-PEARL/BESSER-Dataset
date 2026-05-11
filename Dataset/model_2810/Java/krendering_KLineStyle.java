





import java.util.List;
import java.util.ArrayList;

public class krendering_KLineStyle extends KStyle {

    private float dashOffset;
    private float dashPattern;
    private String lineStyle;



    public krendering_KLineStyle(
        float dashOffset,        float dashPattern,        String lineStyle    ) {
        super(
        );
        this.dashOffset = dashOffset;
        this.dashPattern = dashPattern;
        this.lineStyle = lineStyle;
    }


    public float getDashoffset() {
        return dashOffset;
    }

    public void setDashoffset(float dashOffset) {
        this.dashOffset = dashOffset;
    }
    public float getDashpattern() {
        return dashPattern;
    }

    public void setDashpattern(float dashPattern) {
        this.dashPattern = dashPattern;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }


}