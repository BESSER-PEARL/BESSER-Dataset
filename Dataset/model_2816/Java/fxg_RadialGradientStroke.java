





import java.util.List;
import java.util.ArrayList;

public class fxg_RadialGradientStroke  {

    private String weight;
    private String scaleY;
    private String pixelHinting;
    private String scaleMode;
    private String y;
    private String x;
    private String rotation;
    private String caps;
    private String interpolationMethod;
    private String scaleX;
    private String miterLimit;
    private String joints;
    private String focalPointRatio;
    private String spreadMethod;





    private fxg_Matrix fxg_matrix;


    public fxg_RadialGradientStroke(
        String weight,        String scaleY,        String pixelHinting,        String scaleMode,        String y,        String x,        String rotation,        String caps,        String interpolationMethod,        String scaleX,        String miterLimit,        String joints,        String focalPointRatio,        String spreadMethod    ) {
        this.weight = weight;
        this.scaleY = scaleY;
        this.pixelHinting = pixelHinting;
        this.scaleMode = scaleMode;
        this.y = y;
        this.x = x;
        this.rotation = rotation;
        this.caps = caps;
        this.interpolationMethod = interpolationMethod;
        this.scaleX = scaleX;
        this.miterLimit = miterLimit;
        this.joints = joints;
        this.focalPointRatio = focalPointRatio;
        this.spreadMethod = spreadMethod;
    }


    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getScaley() {
        return scaleY;
    }

    public void setScaley(String scaleY) {
        this.scaleY = scaleY;
    }
    public String getPixelhinting() {
        return pixelHinting;
    }

    public void setPixelhinting(String pixelHinting) {
        this.pixelHinting = pixelHinting;
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
    public String getCaps() {
        return caps;
    }

    public void setCaps(String caps) {
        this.caps = caps;
    }
    public String getInterpolationmethod() {
        return interpolationMethod;
    }

    public void setInterpolationmethod(String interpolationMethod) {
        this.interpolationMethod = interpolationMethod;
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
    public String getJoints() {
        return joints;
    }

    public void setJoints(String joints) {
        this.joints = joints;
    }
    public String getFocalpointratio() {
        return focalPointRatio;
    }

    public void setFocalpointratio(String focalPointRatio) {
        this.focalPointRatio = focalPointRatio;
    }
    public String getSpreadmethod() {
        return spreadMethod;
    }

    public void setSpreadmethod(String spreadMethod) {
        this.spreadMethod = spreadMethod;
    }

    public fxg_Matrix getFxg_matrix() {
        return fxg_matrix;
    }

    public void setFxg_matrix(fxg_Matrix fxg_matrix) {
        this.fxg_matrix = fxg_matrix;
    }

}