





import java.util.List;
import java.util.ArrayList;

public class fxg_RichText extends ParagraphAttributes, FXGElement, ContainerAttributes, CharacterAttributes {

    private String maskType;
    private String scaleX;
    private String y;
    private String height;
    private String x;
    private String rotation;
    private String id;
    private String scaleY;
    private String visible;
    private String width;
    private String alpha;
    private String blendMode;
    private String _tempcontent;



    public fxg_RichText(
        String maskType,        String scaleX,        String y,        String height,        String x,        String rotation,        String id,        String scaleY,        String visible,        String width,        String alpha,        String blendMode,        String _tempcontent    ) {
        super(
        );
        this.maskType = maskType;
        this.scaleX = scaleX;
        this.y = y;
        this.height = height;
        this.x = x;
        this.rotation = rotation;
        this.id = id;
        this.scaleY = scaleY;
        this.visible = visible;
        this.width = width;
        this.alpha = alpha;
        this.blendMode = blendMode;
        this._tempcontent = _tempcontent;
    }


    public String getMasktype() {
        return maskType;
    }

    public void setMasktype(String maskType) {
        this.maskType = maskType;
    }
    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getScaley() {
        return scaleY;
    }

    public void setScaley(String scaleY) {
        this.scaleY = scaleY;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getBlendmode() {
        return blendMode;
    }

    public void setBlendmode(String blendMode) {
        this.blendMode = blendMode;
    }
    public String get_tempcontent() {
        return _tempcontent;
    }

    public void set_tempcontent(String _tempcontent) {
        this._tempcontent = _tempcontent;
    }


}