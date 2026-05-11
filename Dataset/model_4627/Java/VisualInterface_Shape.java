





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Shape extends Figure {

    private String antialias;
    private boolean outline;
    private boolean fill;
    private String alpha;
    private float lineWidth;



    public VisualInterface_Shape(
        String antialias,        boolean outline,        boolean fill,        String alpha,        float lineWidth    ) {
        super(
        );
        this.antialias = antialias;
        this.outline = outline;
        this.fill = fill;
        this.alpha = alpha;
        this.lineWidth = lineWidth;
    }


    public String getAntialias() {
        return antialias;
    }

    public void setAntialias(String antialias) {
        this.antialias = antialias;
    }
    public boolean getOutline() {
        return outline;
    }

    public void setOutline(boolean outline) {
        this.outline = outline;
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
    public float getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(float lineWidth) {
        this.lineWidth = lineWidth;
    }


}