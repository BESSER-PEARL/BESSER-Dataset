





import java.util.List;
import java.util.ArrayList;

public class fxg_LinearGradientStroke  {

    private String interpolationMethod;
    private String miterLimit;
    private String scaleMode;
    private String y;
    private String weight;
    private String scaleX;
    private String spreadMethod;
    private String joints;
    private String x;
    private String pixelHinting;
    private String caps;
    private String rotation;





    private fxg_Matrix fxg_matrix;


    public fxg_LinearGradientStroke(
        String interpolationMethod,        String miterLimit,        String scaleMode,        String y,        String weight,        String scaleX,        String spreadMethod,        String joints,        String x,        String pixelHinting,        String caps,        String rotation    ) {
        this.interpolationMethod = interpolationMethod;
        this.miterLimit = miterLimit;
        this.scaleMode = scaleMode;
        this.y = y;
        this.weight = weight;
        this.scaleX = scaleX;
        this.spreadMethod = spreadMethod;
        this.joints = joints;
        this.x = x;
        this.pixelHinting = pixelHinting;
        this.caps = caps;
        this.rotation = rotation;
    }


    public String getInterpolationmethod() {
        return interpolationMethod;
    }

    public void setInterpolationmethod(String interpolationMethod) {
        this.interpolationMethod = interpolationMethod;
    }
    public String getMiterlimit() {
        return miterLimit;
    }

    public void setMiterlimit(String miterLimit) {
        this.miterLimit = miterLimit;
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
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getSpreadmethod() {
        return spreadMethod;
    }

    public void setSpreadmethod(String spreadMethod) {
        this.spreadMethod = spreadMethod;
    }
    public String getJoints() {
        return joints;
    }

    public void setJoints(String joints) {
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
    public String getCaps() {
        return caps;
    }

    public void setCaps(String caps) {
        this.caps = caps;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }

    public fxg_Matrix getFxg_matrix() {
        return fxg_matrix;
    }

    public void setFxg_matrix(fxg_Matrix fxg_matrix) {
        this.fxg_matrix = fxg_matrix;
    }

}