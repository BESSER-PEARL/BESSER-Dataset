





import java.util.List;
import java.util.ArrayList;

public class fxg_Line extends Shape {

    private String xFrom;
    private String blendMode;
    private String xTo;
    private String scaleX;
    private String yTo;
    private String id;
    private String y;
    private String rotation;
    private String x;
    private String maskType;
    private String yFrom;
    private String alpha;
    private String scaleY;
    private String visible;





    private fxg_Group fxg_group;




    private List<fxg_Filter> fxg_filters;




    private fxg_Stroke fxg_stroke;




    private fxg_Fill fxg_fill;




    private fxg_Transform fxg_transform;


    public fxg_Line(
        String xFrom,        String blendMode,        String xTo,        String scaleX,        String yTo,        String id,        String y,        String rotation,        String x,        String maskType,        String yFrom,        String alpha,        String scaleY,        String visible    ) {
        super(
        );
        this.xFrom = xFrom;
        this.blendMode = blendMode;
        this.xTo = xTo;
        this.scaleX = scaleX;
        this.yTo = yTo;
        this.id = id;
        this.y = y;
        this.rotation = rotation;
        this.x = x;
        this.maskType = maskType;
        this.yFrom = yFrom;
        this.alpha = alpha;
        this.scaleY = scaleY;
        this.visible = visible;
        this.fxg_filters = new ArrayList<>();
    }

    public fxg_Line(
        String xFrom,        String blendMode,        String xTo,        String scaleX,        String yTo,        String id,        String y,        String rotation,        String x,        String maskType,        String yFrom,        String alpha,        String scaleY,        String visible        ArrayList<fxg_Filter> fxg_filters    ) {
        this.xFrom = xFrom;
        this.blendMode = blendMode;
        this.xTo = xTo;
        this.scaleX = scaleX;
        this.yTo = yTo;
        this.id = id;
        this.y = y;
        this.rotation = rotation;
        this.x = x;
        this.maskType = maskType;
        this.yFrom = yFrom;
        this.alpha = alpha;
        this.scaleY = scaleY;
        this.visible = visible;
        this.fxg_filters = fxg_filters;
    }

    public String getXfrom() {
        return xFrom;
    }

    public void setXfrom(String xFrom) {
        this.xFrom = xFrom;
    }
    public String getBlendmode() {
        return blendMode;
    }

    public void setBlendmode(String blendMode) {
        this.blendMode = blendMode;
    }
    public String getXto() {
        return xTo;
    }

    public void setXto(String xTo) {
        this.xTo = xTo;
    }
    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getYto() {
        return yTo;
    }

    public void setYto(String yTo) {
        this.yTo = yTo;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getMasktype() {
        return maskType;
    }

    public void setMasktype(String maskType) {
        this.maskType = maskType;
    }
    public String getYfrom() {
        return yFrom;
    }

    public void setYfrom(String yFrom) {
        this.yFrom = yFrom;
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
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }

    public fxg_Group getFxg_group() {
        return fxg_group;
    }

    public void setFxg_group(fxg_Group fxg_group) {
        this.fxg_group = fxg_group;
    }
    public List<fxg_Filter> getFxg_filters() {
        return fxg_filters;
    }

    public void addFxg_filter(Fxg_filter fxg_filter) {
        this.fxg_filters.add(fxg_filter);
    }
    public fxg_Stroke getFxg_stroke() {
        return fxg_stroke;
    }

    public void setFxg_stroke(fxg_Stroke fxg_stroke) {
        this.fxg_stroke = fxg_stroke;
    }
    public fxg_Fill getFxg_fill() {
        return fxg_fill;
    }

    public void setFxg_fill(fxg_Fill fxg_fill) {
        this.fxg_fill = fxg_fill;
    }
    public fxg_Transform getFxg_transform() {
        return fxg_transform;
    }

    public void setFxg_transform(fxg_Transform fxg_transform) {
        this.fxg_transform = fxg_transform;
    }

}