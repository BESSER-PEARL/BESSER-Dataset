





import java.util.List;
import java.util.ArrayList;

public class model_Shape extends Figure {

    private boolean fill;
    private String antialias;
    private float lineWidth;
    private String alpha;
    private boolean outline;



    public model_Shape(
        boolean fill,        String antialias,        float lineWidth,        String alpha,        boolean outline    ) {
        super(
        );
        this.fill = fill;
        this.antialias = antialias;
        this.lineWidth = lineWidth;
        this.alpha = alpha;
        this.outline = outline;
    }


    public boolean getFill() {
        return fill;
    }

    public void setFill(boolean fill) {
        this.fill = fill;
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
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public boolean getOutline() {
        return outline;
    }

    public void setOutline(boolean outline) {
        this.outline = outline;
    }


}