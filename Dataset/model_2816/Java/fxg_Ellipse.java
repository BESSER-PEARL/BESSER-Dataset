





import java.util.List;
import java.util.ArrayList;

public class fxg_Ellipse extends Shape {

    private String scaleX;
    private String y;
    private String rotation;
    private String alpha;
    private String width;
    private String blendMode;
    private String height;
    private String visible;
    private String x;
    private String scaleY;





    private fxg_Transform fxg_transform;




    private fxg_Stroke fxg_stroke;




    private List<fxg_Filter> fxg_filters;




    private fxg_Group fxg_group;




    private fxg_Fill fxg_fill;


    public fxg_Ellipse(
        String scaleX,        String y,        String rotation,        String alpha,        String width,        String blendMode,        String height,        String visible,        String x,        String scaleY    ) {
        super(
        );
        this.scaleX = scaleX;
        this.y = y;
        this.rotation = rotation;
        this.alpha = alpha;
        this.width = width;
        this.blendMode = blendMode;
        this.height = height;
        this.visible = visible;
        this.x = x;
        this.scaleY = scaleY;
        this.fxg_filters = new ArrayList<>();
    }

    public fxg_Ellipse(
        String scaleX,        String y,        String rotation,        String alpha,        String width,        String blendMode,        String height,        String visible,        String x,        String scaleY        ArrayList<fxg_Filter> fxg_filters    ) {
        this.scaleX = scaleX;
        this.y = y;
        this.rotation = rotation;
        this.alpha = alpha;
        this.width = width;
        this.blendMode = blendMode;
        this.height = height;
        this.visible = visible;
        this.x = x;
        this.scaleY = scaleY;
        this.fxg_filters = fxg_filters;
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

    public fxg_Transform getFxg_transform() {
        return fxg_transform;
    }

    public void setFxg_transform(fxg_Transform fxg_transform) {
        this.fxg_transform = fxg_transform;
    }
    public fxg_Stroke getFxg_stroke() {
        return fxg_stroke;
    }

    public void setFxg_stroke(fxg_Stroke fxg_stroke) {
        this.fxg_stroke = fxg_stroke;
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
    public fxg_Fill getFxg_fill() {
        return fxg_fill;
    }

    public void setFxg_fill(fxg_Fill fxg_fill) {
        this.fxg_fill = fxg_fill;
    }

}