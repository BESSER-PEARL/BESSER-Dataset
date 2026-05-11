





import java.util.List;
import java.util.ArrayList;

public class fxg_LinearGradientStroke  {

    private String scaleX;
    private String pixelHinting;
    private String interpolationMethod;
    private String y;
    private String scaleMode;
    private String x;
    private String miterLimit;
    private String weight;
    private String rotation;
    private String spreadMethod;
    private String joints;
    private String caps;





    private fxg_Matrix fxg_matrix;


    public fxg_LinearGradientStroke(
        String scaleX,        String pixelHinting,        String interpolationMethod,        String y,        String scaleMode,        String x,        String miterLimit,        String weight,        String rotation,        String spreadMethod,        String joints,        String caps    ) {
        this.scaleX = scaleX;
        this.pixelHinting = pixelHinting;
        this.interpolationMethod = interpolationMethod;
        this.y = y;
        this.scaleMode = scaleMode;
        this.x = x;
        this.miterLimit = miterLimit;
        this.weight = weight;
        this.rotation = rotation;
        this.spreadMethod = spreadMethod;
        this.joints = joints;
        this.caps = caps;
    }


    public String getScalex() {
        return scaleX;
    }

    public void setScalex(String scaleX) {
        this.scaleX = scaleX;
    }
    public String getPixelhinting() {
        return pixelHinting;
    }

    public void setPixelhinting(String pixelHinting) {
        this.pixelHinting = pixelHinting;
    }
    public String getInterpolationmethod() {
        return interpolationMethod;
    }

    public void setInterpolationmethod(String interpolationMethod) {
        this.interpolationMethod = interpolationMethod;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getScalemode() {
        return scaleMode;
    }

    public void setScalemode(String scaleMode) {
        this.scaleMode = scaleMode;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getMiterlimit() {
        return miterLimit;
    }

    public void setMiterlimit(String miterLimit) {
        this.miterLimit = miterLimit;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
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
    public String getCaps() {
        return caps;
    }

    public void setCaps(String caps) {
        this.caps = caps;
    }

    public fxg_Matrix getFxg_matrix() {
        return fxg_matrix;
    }

    public void setFxg_matrix(fxg_Matrix fxg_matrix) {
        this.fxg_matrix = fxg_matrix;
    }

}