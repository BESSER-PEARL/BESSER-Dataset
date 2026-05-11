





import java.util.List;
import java.util.ArrayList;

public class fxg_RichText extends CharacterAttributes, ParagraphAttributes, ContainerAttributes, FXGElement {

    private String rotation;
    private String alpha;
    private String scaleY;
    private String width;
    private String maskType;
    private String _tempcontent;
    private String y;
    private String id;
    private String scaleX;
    private String x;
    private String blendMode;
    private String height;
    private String visible;



    public fxg_RichText(
        String rotation,        String alpha,        String scaleY,        String width,        String maskType,        String _tempcontent,        String y,        String id,        String scaleX,        String x,        String blendMode,        String height,        String visible    ) {
        super(
        );
        this.rotation = rotation;
        this.alpha = alpha;
        this.scaleY = scaleY;
        this.width = width;
        this.maskType = maskType;
        this._tempcontent = _tempcontent;
        this.y = y;
        this.id = id;
        this.scaleX = scaleX;
        this.x = x;
        this.blendMode = blendMode;
        this.height = height;
        this.visible = visible;
    }


    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
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
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getMasktype() {
        return maskType;
    }

    public void setMasktype(String maskType) {
        this.maskType = maskType;
    }
    public String get_tempcontent() {
        return _tempcontent;
    }

    public void set_tempcontent(String _tempcontent) {
        this._tempcontent = _tempcontent;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getBlendmode() {
        return blendMode;
    }

    public void setBlendmode(String blendMode) {
        this.blendMode = blendMode;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }


}