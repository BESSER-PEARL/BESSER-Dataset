





import java.util.List;
import java.util.ArrayList;

public class model_Shape extends Figure {

    private boolean outline;
    private String alpha;
    private String antialias;
    private float lineWidth;
    private boolean fill;



    public model_Shape(
        boolean outline,        String alpha,        String antialias,        float lineWidth,        boolean fill    ) {
        super(
        );
        this.outline = outline;
        this.alpha = alpha;
        this.antialias = antialias;
        this.lineWidth = lineWidth;
        this.fill = fill;
    }


    public boolean getOutline() {
        return outline;
    }

    public void setOutline(boolean outline) {
        this.outline = outline;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
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


}