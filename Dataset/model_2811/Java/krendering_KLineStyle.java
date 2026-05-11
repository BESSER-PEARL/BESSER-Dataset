





import java.util.List;
import java.util.ArrayList;

public class krendering_KLineStyle extends KStyle {

    private String lineStyle;
    private float dashOffset;
    private float dashPattern;



    public krendering_KLineStyle(
        String lineStyle,        float dashOffset,        float dashPattern    ) {
        super(
        );
        this.lineStyle = lineStyle;
        this.dashOffset = dashOffset;
        this.dashPattern = dashPattern;
    }


    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
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


}