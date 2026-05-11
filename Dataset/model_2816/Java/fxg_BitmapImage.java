





import java.util.List;
import java.util.ArrayList;

public class fxg_BitmapImage extends FXGElement {

    private String visible;
    private String rotation;
    private String height;
    private String fillMode;
    private String x;
    private String scaleY;
    private String scaleX;
    private String source;
    private String y;
    private String alpha;
    private String width;
    private String blendMode;



    public fxg_BitmapImage(
        String visible,        String rotation,        String height,        String fillMode,        String x,        String scaleY,        String scaleX,        String source,        String y,        String alpha,        String width,        String blendMode    ) {
        super(
        );
        this.visible = visible;
        this.rotation = rotation;
        this.height = height;
        this.fillMode = fillMode;
        this.x = x;
        this.scaleY = scaleY;
        this.scaleX = scaleX;
        this.source = source;
        this.y = y;
        this.alpha = alpha;
        this.width = width;
        this.blendMode = blendMode;
    }


    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
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
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getScaley() {
        return scaleY;
    }

    public void setScaley(String scaleY) {
        this.scaleY = scaleY;
    }
    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getBlendmode() {
        return blendMode;
    }

    public void setBlendmode(String blendMode) {
        this.blendMode = blendMode;
    }


}