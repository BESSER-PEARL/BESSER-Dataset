





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Shape extends Figure {

    private boolean outline;
    private String antialias;
    private float lineWidth;
    private boolean fill;
    private String alpha;



    public VisualInterface_Shape(
        boolean outline,        String antialias,        float lineWidth,        boolean fill,        String alpha    ) {
        super(
        );
        this.outline = outline;
        this.antialias = antialias;
        this.lineWidth = lineWidth;
        this.fill = fill;
        this.alpha = alpha;
    }


    public boolean getOutline() {
        return outline;
    }

    public void setOutline(boolean outline) {
        this.outline = outline;
    }
    public String getAntialias() {
        return antialias;
    }

    public void setAntialias(String antialias) {
        this.antialias = antialias;
    }
    public float getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(float lineWidth) {
        this.lineWidth = lineWidth;
    }
    public boolean getFill() {
        return fill;
    }

    public void setFill(boolean fill) {
        this.fill = fill;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }


}