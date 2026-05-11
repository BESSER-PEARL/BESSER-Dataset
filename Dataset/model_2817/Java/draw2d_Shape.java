





import java.util.List;
import java.util.ArrayList;

public class draw2d_Shape extends Figure {

    private boolean outline;
    private float lineWidthFloat;
    private String lineStyle;
    private String lineCap;
    private float lineMiterLimit;
    private String alpha;
    private String antialias;
    private float lineDash;
    private boolean fillXOR;
    private float lineDashOffset;
    private boolean fill;
    private String lineJoin;
    private boolean outlineXOR;



    public draw2d_Shape(
        boolean outline,        float lineWidthFloat,        String lineStyle,        String lineCap,        float lineMiterLimit,        String alpha,        String antialias,        float lineDash,        boolean fillXOR,        float lineDashOffset,        boolean fill,        String lineJoin,        boolean outlineXOR    ) {
        super(
        );
        this.outline = outline;
        this.lineWidthFloat = lineWidthFloat;
        this.lineStyle = lineStyle;
        this.lineCap = lineCap;
        this.lineMiterLimit = lineMiterLimit;
        this.alpha = alpha;
        this.antialias = antialias;
        this.lineDash = lineDash;
        this.fillXOR = fillXOR;
        this.lineDashOffset = lineDashOffset;
        this.fill = fill;
        this.lineJoin = lineJoin;
        this.outlineXOR = outlineXOR;
    }


    public boolean getOutline() {
        return outline;
    }

    public void setOutline(boolean outline) {
        this.outline = outline;
    }
    public float getLinewidthfloat() {
        return lineWidthFloat;
    }

    public void setLinewidthfloat(float lineWidthFloat) {
        this.lineWidthFloat = lineWidthFloat;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getLinecap() {
        return lineCap;
    }

    public void setLinecap(String lineCap) {
        this.lineCap = lineCap;
    }
    public float getLinemiterlimit() {
        return lineMiterLimit;
    }

    public void setLinemiterlimit(float lineMiterLimit) {
        this.lineMiterLimit = lineMiterLimit;
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
    public float getLinedash() {
        return lineDash;
    }

    public void setLinedash(float lineDash) {
        this.lineDash = lineDash;
    }
    public boolean getFillxor() {
        return fillXOR;
    }

    public void setFillxor(boolean fillXOR) {
        this.fillXOR = fillXOR;
    }
    public float getLinedashoffset() {
        return lineDashOffset;
    }

    public void setLinedashoffset(float lineDashOffset) {
        this.lineDashOffset = lineDashOffset;
    }
    public boolean getFill() {
        return fill;
    }

    public void setFill(boolean fill) {
        this.fill = fill;
    }
    public String getLinejoin() {
        return lineJoin;
    }

    public void setLinejoin(String lineJoin) {
        this.lineJoin = lineJoin;
    }
    public boolean getOutlinexor() {
        return outlineXOR;
    }

    public void setOutlinexor(boolean outlineXOR) {
        this.outlineXOR = outlineXOR;
    }


}