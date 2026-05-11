





import java.util.List;
import java.util.ArrayList;

public class fxg_RadialGradientStroke  {

    private String x;
    private String pixelHinting;
    private String weight;
    private String spreadMethod;
    private String scaleMode;
    private String y;
    private String rotation;
    private String caps;
    private String scaleY;
    private String scaleX;
    private String miterLimit;
    private String interpolationMethod;
    private String focalPointRatio;
    private String joints;





    private fxg_Matrix fxg_matrix;


    public fxg_RadialGradientStroke(
        String x,        String pixelHinting,        String weight,        String spreadMethod,        String scaleMode,        String y,        String rotation,        String caps,        String scaleY,        String scaleX,        String miterLimit,        String interpolationMethod,        String focalPointRatio,        String joints    ) {
        this.x = x;
        this.pixelHinting = pixelHinting;
        this.weight = weight;
        this.spreadMethod = spreadMethod;
        this.scaleMode = scaleMode;
        this.y = y;
        this.rotation = rotation;
        this.caps = caps;
        this.scaleY = scaleY;
        this.scaleX = scaleX;
        this.miterLimit = miterLimit;
        this.interpolationMethod = interpolationMethod;
        this.focalPointRatio = focalPointRatio;
        this.joints = joints;
    }


    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getPixelhinting() {
        return pixelHinting;
    }

    public void setPixelhinting(String pixelHinting) {
        this.pixelHinting = pixelHinting;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getSpreadmethod() {
        return spreadMethod;
    }

    public void setSpreadmethod(String spreadMethod) {
        this.spreadMethod = spreadMethod;
    }
    public String getScalemode() {
        return scaleMode;
    }

    public void setScalemode(String scaleMode) {
        this.scaleMode = scaleMode;
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
    public String getCaps() {
        return caps;
    }

    public void setCaps(String caps) {
        this.caps = caps;
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
    public String getMiterlimit() {
        return miterLimit;
    }

    public void setMiterlimit(String miterLimit) {
        this.miterLimit = miterLimit;
    }
    public String getInterpolationmethod() {
        return interpolationMethod;
    }

    public void setInterpolationmethod(String interpolationMethod) {
        this.interpolationMethod = interpolationMethod;
    }
    public String getFocalpointratio() {
        return focalPointRatio;
    }

    public void setFocalpointratio(String focalPointRatio) {
        this.focalPointRatio = focalPointRatio;
    }
    public String getJoints() {
        return joints;
    }

    public void setJoints(String joints) {
        this.joints = joints;
    }

    public fxg_Matrix getFxg_matrix() {
        return fxg_matrix;
    }

    public void setFxg_matrix(fxg_Matrix fxg_matrix) {
        this.fxg_matrix = fxg_matrix;
    }

}