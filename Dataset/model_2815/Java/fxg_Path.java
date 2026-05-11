





import java.util.List;
import java.util.ArrayList;

public class fxg_Path extends FXGElement {

    private String scaleY;
    private String scaleX;
    private String y;
    private String alpha;
    private String blendMode;
    private String visible;
    private String rotation;
    private String data;
    private String x;
    private String winding;





    private List<fxg_Filter> fxg_filters;




    private fxg_Group fxg_group;


    public fxg_Path(
        String scaleY,        String scaleX,        String y,        String alpha,        String blendMode,        String visible,        String rotation,        String data,        String x,        String winding    ) {
        super(
        );
        this.scaleY = scaleY;
        this.scaleX = scaleX;
        this.y = y;
        this.alpha = alpha;
        this.blendMode = blendMode;
        this.visible = visible;
        this.rotation = rotation;
        this.data = data;
        this.x = x;
        this.winding = winding;
        this.fxg_filters = new ArrayList<>();
    }

    public fxg_Path(
        String scaleY,        String scaleX,        String y,        String alpha,        String blendMode,        String visible,        String rotation,        String data,        String x,        String winding        ArrayList<fxg_Filter> fxg_filters    ) {
        this.scaleY = scaleY;
        this.scaleX = scaleX;
        this.y = y;
        this.alpha = alpha;
        this.blendMode = blendMode;
        this.visible = visible;
        this.rotation = rotation;
        this.data = data;
        this.x = x;
        this.winding = winding;
        this.fxg_filters = fxg_filters;
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
    public String getBlendmode() {
        return blendMode;
    }

    public void setBlendmode(String blendMode) {
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
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
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

    public List<fxg_Filter> getFxg_filters() {
        return fxg_filters;
    }

    public void addFxg_filter(Fxg_filter fxg_filter) {
        this.fxg_filters.add(fxg_filter);
    }
    public fxg_Group getFxg_group() {
        return fxg_group;
    }

    public void setFxg_group(fxg_Group fxg_group) {
        this.fxg_group = fxg_group;
    }

}