





import java.util.List;
import java.util.ArrayList;

public class fxg_Path extends FXGElement {

    private String visible;
    private String data;
    private String scaleX;
    private String blendMode;
    private String rotation;
    private String scaleY;
    private String alpha;
    private String y;
    private String x;
    private String winding;





    private fxg_Group fxg_group;


    public fxg_Path(
        String visible,        String data,        String scaleX,        String blendMode,        String rotation,        String scaleY,        String alpha,        String y,        String x,        String winding    ) {
        super(
        );
        this.visible = visible;
        this.data = data;
        this.scaleX = scaleX;
        this.blendMode = blendMode;
        this.rotation = rotation;
        this.scaleY = scaleY;
        this.alpha = alpha;
        this.y = y;
        this.x = x;
        this.winding = winding;
    }


    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
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
    public String getScaley() {
        return scaleY;
    }

    public void setScaley(String scaleY) {
        this.scaleY = scaleY;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getWinding() {
        return winding;
    }

    public void setWinding(String winding) {
        this.winding = winding;
    }

    public fxg_Group getFxg_group() {
        return fxg_group;
    }

    public void setFxg_group(fxg_Group fxg_group) {
        this.fxg_group = fxg_group;
    }

}