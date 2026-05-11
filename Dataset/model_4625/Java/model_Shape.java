





import java.util.List;
import java.util.ArrayList;

public class model_Shape extends Figure {

    private float lineWidth;
    private boolean outline;
    private String antialias;
    private boolean fill;
    private String alpha;



    public model_Shape(
        float lineWidth,        boolean outline,        String antialias,        boolean fill,        String alpha    ) {
        super(
        );
        this.lineWidth = lineWidth;
        this.outline = outline;
        this.antialias = antialias;
        this.fill = fill;
        this.alpha = alpha;
    }


    public float getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(float lineWidth) {
        this.lineWidth = lineWidth;
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