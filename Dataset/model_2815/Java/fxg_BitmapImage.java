





import java.util.List;
import java.util.ArrayList;

public class fxg_BitmapImage extends FXGElement {

    private String scaleX;
    private String width;
    private String source;
    private String height;
    private String fillMode;
    private String blendMode;
    private String rotation;
    private String visible;
    private String alpha;
    private String scaleY;
    private String x;
    private String y;



    public fxg_BitmapImage(
        String scaleX,        String width,        String source,        String height,        String fillMode,        String blendMode,        String rotation,        String visible,        String alpha,        String scaleY,        String x,        String y    ) {
        super(
        );
        this.scaleX = scaleX;
        this.width = width;
        this.source = source;
        this.height = height;
        this.fillMode = fillMode;
        this.blendMode = blendMode;
        this.rotation = rotation;
        this.visible = visible;
        this.alpha = alpha;
        this.scaleY = scaleY;
        this.x = x;
        this.y = y;
    }


    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getFillmode() {
        return fillMode;
    }

    public void setFillmode(String fillMode) {
        this.fillMode = fillMode;
    }
    public String getBlendmode() {
        return blendMode;
    }

    public void setBlendmode(String blendMode) {
        this.blendMode = blendMode;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getScaley() {
        return scaleY;
    }

    public void setScaley(String scaleY) {
        this.scaleY = scaleY;
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


}