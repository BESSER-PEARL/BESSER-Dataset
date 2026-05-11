





import java.util.List;
import java.util.ArrayList;

public class fxg_Rect extends Shape {

    private String scaleX;
    private String height;
    private String bottomRightRadiusY;
    private String scaleY;
    private String topLeftRadiusX;
    private String topRightRadiusY;
    private String alpha;
    private String visible;
    private String width;
    private String bottomRightRadiusX;
    private String blendMode;
    private String radiusX;
    private String topLeftRadiusY;
    private String x;
    private String y;
    private String radiusY;
    private String bottomLeftRadiusX;
    private String topRightRadiusX;
    private String rotation;
    private String bottomLeftRadiusY;





    private fxg_Stroke fxg_stroke;




    private fxg_Group fxg_group;




    private List<fxg_Filter> fxg_filters;




    private fxg_Fill fxg_fill;




    private fxg_Transform fxg_transform;


    public fxg_Rect(
        String scaleX,        String height,        String bottomRightRadiusY,        String scaleY,        String topLeftRadiusX,        String topRightRadiusY,        String alpha,        String visible,        String width,        String bottomRightRadiusX,        String blendMode,        String radiusX,        String topLeftRadiusY,        String x,        String y,        String radiusY,        String bottomLeftRadiusX,        String topRightRadiusX,        String rotation,        String bottomLeftRadiusY    ) {
        super(
        );
        this.scaleX = scaleX;
        this.height = height;
        this.bottomRightRadiusY = bottomRightRadiusY;
        this.scaleY = scaleY;
        this.topLeftRadiusX = topLeftRadiusX;
        this.topRightRadiusY = topRightRadiusY;
        this.alpha = alpha;
        this.visible = visible;
        this.width = width;
        this.bottomRightRadiusX = bottomRightRadiusX;
        this.blendMode = blendMode;
        this.radiusX = radiusX;
        this.topLeftRadiusY = topLeftRadiusY;
        this.x = x;
        this.y = y;
        this.radiusY = radiusY;
        this.bottomLeftRadiusX = bottomLeftRadiusX;
        this.topRightRadiusX = topRightRadiusX;
        this.rotation = rotation;
        this.bottomLeftRadiusY = bottomLeftRadiusY;
        this.fxg_filters = new ArrayList<>();
    }

    public fxg_Rect(
        String scaleX,        String height,        String bottomRightRadiusY,        String scaleY,        String topLeftRadiusX,        String topRightRadiusY,        String alpha,        String visible,        String width,        String bottomRightRadiusX,        String blendMode,        String radiusX,        String topLeftRadiusY,        String x,        String y,        String radiusY,        String bottomLeftRadiusX,        String topRightRadiusX,        String rotation,        String bottomLeftRadiusY        ArrayList<fxg_Filter> fxg_filters    ) {
        this.scaleX = scaleX;
        this.height = height;
        this.bottomRightRadiusY = bottomRightRadiusY;
        this.scaleY = scaleY;
        this.topLeftRadiusX = topLeftRadiusX;
        this.topRightRadiusY = topRightRadiusY;
        this.alpha = alpha;
        this.visible = visible;
        this.width = width;
        this.bottomRightRadiusX = bottomRightRadiusX;
        this.blendMode = blendMode;
        this.radiusX = radiusX;
        this.topLeftRadiusY = topLeftRadiusY;
        this.x = x;
        this.y = y;
        this.radiusY = radiusY;
        this.bottomLeftRadiusX = bottomLeftRadiusX;
        this.topRightRadiusX = topRightRadiusX;
        this.rotation = rotation;
        this.bottomLeftRadiusY = bottomLeftRadiusY;
        this.fxg_filters = fxg_filters;
    }

    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getBottomrightradiusy() {
        return bottomRightRadiusY;
    }

    public void setBottomrightradiusy(String bottomRightRadiusY) {
        this.bottomRightRadiusY = bottomRightRadiusY;
    }
    public String getScaley() {
        return scaleY;
    }

    public void setScaley(String scaleY) {
        this.scaleY = scaleY;
    }
    public String getTopleftradiusx() {
        return topLeftRadiusX;
    }

    public void setTopleftradiusx(String topLeftRadiusX) {
        this.topLeftRadiusX = topLeftRadiusX;
    }
    public String getToprightradiusy() {
        return topRightRadiusY;
    }

    public void setToprightradiusy(String topRightRadiusY) {
        this.topRightRadiusY = topRightRadiusY;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
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
    public String getBottomrightradiusx() {
        return bottomRightRadiusX;
    }

    public void setBottomrightradiusx(String bottomRightRadiusX) {
        this.bottomRightRadiusX = bottomRightRadiusX;
    }
    public String getBlendmode() {
        return blendMode;
    }

    public void setBlendmode(String blendMode) {
        this.blendMode = blendMode;
    }
    public String getRadiusx() {
        return radiusX;
    }

    public void setRadiusx(String radiusX) {
        this.radiusX = radiusX;
    }
    public String getTopleftradiusy() {
        return topLeftRadiusY;
    }

    public void setTopleftradiusy(String topLeftRadiusY) {
        this.topLeftRadiusY = topLeftRadiusY;
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
    public String getRadiusy() {
        return radiusY;
    }

    public void setRadiusy(String radiusY) {
        this.radiusY = radiusY;
    }
    public String getBottomleftradiusx() {
        return bottomLeftRadiusX;
    }

    public void setBottomleftradiusx(String bottomLeftRadiusX) {
        this.bottomLeftRadiusX = bottomLeftRadiusX;
    }
    public String getToprightradiusx() {
        return topRightRadiusX;
    }

    public void setToprightradiusx(String topRightRadiusX) {
        this.topRightRadiusX = topRightRadiusX;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getBottomleftradiusy() {
        return bottomLeftRadiusY;
    }

    public void setBottomleftradiusy(String bottomLeftRadiusY) {
        this.bottomLeftRadiusY = bottomLeftRadiusY;
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
    public List<fxg_Filter> getFxg_filters() {
        return fxg_filters;
    }

    public void addFxg_filter(Fxg_filter fxg_filter) {
        this.fxg_filters.add(fxg_filter);
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