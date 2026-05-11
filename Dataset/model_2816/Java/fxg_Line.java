





import java.util.List;
import java.util.ArrayList;

public class fxg_Line extends Shape {

    private String blendMode;
    private String yFrom;
    private String xTo;
    private String rotation;
    private String id;
    private String yTo;
    private String visible;
    private String maskType;
    private String x;
    private String y;
    private String xFrom;
    private String scaleY;
    private String scaleX;
    private String alpha;





    private fxg_Stroke fxg_stroke;




    private fxg_Group fxg_group;




    private fxg_Transform fxg_transform;




    private fxg_Fill fxg_fill;




    private List<fxg_Filter> fxg_filters;


    public fxg_Line(
        String blendMode,        String yFrom,        String xTo,        String rotation,        String id,        String yTo,        String visible,        String maskType,        String x,        String y,        String xFrom,        String scaleY,        String scaleX,        String alpha    ) {
        super(
        );
        this.blendMode = blendMode;
        this.yFrom = yFrom;
        this.xTo = xTo;
        this.rotation = rotation;
        this.id = id;
        this.yTo = yTo;
        this.visible = visible;
        this.maskType = maskType;
        this.x = x;
        this.y = y;
        this.xFrom = xFrom;
        this.scaleY = scaleY;
        this.scaleX = scaleX;
        this.alpha = alpha;
        this.fxg_filters = new ArrayList<>();
    }

    public fxg_Line(
        String blendMode,        String yFrom,        String xTo,        String rotation,        String id,        String yTo,        String visible,        String maskType,        String x,        String y,        String xFrom,        String scaleY,        String scaleX,        String alpha        ArrayList<fxg_Filter> fxg_filters    ) {
        this.blendMode = blendMode;
        this.yFrom = yFrom;
        this.xTo = xTo;
        this.rotation = rotation;
        this.id = id;
        this.yTo = yTo;
        this.visible = visible;
        this.maskType = maskType;
        this.x = x;
        this.y = y;
        this.xFrom = xFrom;
        this.scaleY = scaleY;
        this.scaleX = scaleX;
        this.alpha = alpha;
        this.fxg_filters = fxg_filters;
    }

    public String getBlendmode() {
        return blendMode;
    }

    public void setBlendmode(String blendMode) {
        this.blendMode = blendMode;
    }
    public String getYfrom() {
        return yFrom;
    }

    public void setYfrom(String yFrom) {
        this.yFrom = yFrom;
    }
    public String getXto() {
        return xTo;
    }

    public void setXto(String xTo) {
        this.xTo = xTo;
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
    public String getYto() {
        return yTo;
    }

    public void setYto(String yTo) {
        this.yTo = yTo;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getMasktype() {
        return maskType;
    }

    public void setMasktype(String maskType) {
        this.maskType = maskType;
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
    public String getXfrom() {
        return xFrom;
    }

    public void setXfrom(String xFrom) {
        this.xFrom = xFrom;
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
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }

    public fxg_Stroke getFxg_stroke() {
        return fxg_stroke;
    }

    public void setFxg_stroke(fxg_Stroke fxg_stroke) {
        this.fxg_stroke = fxg_stroke;
    }
    public fxg_Group getFxg_group() {
        return fxg_group;
    }

    public void setFxg_group(fxg_Group fxg_group) {
        this.fxg_group = fxg_group;
    }
    public fxg_Transform getFxg_transform() {
        return fxg_transform;
    }

    public void setFxg_transform(fxg_Transform fxg_transform) {
        this.fxg_transform = fxg_transform;
    }
    public fxg_Fill getFxg_fill() {
        return fxg_fill;
    }

    public void setFxg_fill(fxg_Fill fxg_fill) {
        this.fxg_fill = fxg_fill;
    }
    public List<fxg_Filter> getFxg_filters() {
        return fxg_filters;
    }

    public void addFxg_filter(Fxg_filter fxg_filter) {
        this.fxg_filters.add(fxg_filter);
    }

}