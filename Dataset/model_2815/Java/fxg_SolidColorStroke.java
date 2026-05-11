





import java.util.List;
import java.util.ArrayList;

public class fxg_SolidColorStroke extends Stroke {

    private String miterLimit;
    private String caps;
    private String scaleMode;
    private String joints;
    private String color;
    private String weight;
    private String pixelHinting;
    private String alpha;



    public fxg_SolidColorStroke(
        String miterLimit,        String caps,        String scaleMode,        String joints,        String color,        String weight,        String pixelHinting,        String alpha    ) {
        super(
        );
        this.miterLimit = miterLimit;
        this.caps = caps;
        this.scaleMode = scaleMode;
        this.joints = joints;
        this.color = color;
        this.weight = weight;
        this.pixelHinting = pixelHinting;
        this.alpha = alpha;
    }


    public String getMiterlimit() {
        return miterLimit;
    }

    public void setMiterlimit(String miterLimit) {
        this.miterLimit = miterLimit;
    }
    public String getCaps() {
        return caps;
    }

    public void setCaps(String caps) {
        this.caps = caps;
    }
    public String getScalemode() {
        return scaleMode;
    }

    public void setScalemode(String scaleMode) {
        this.scaleMode = scaleMode;
    }
    public String getJoints() {
        return joints;
    }

    public void setJoints(String joints) {
        this.joints = joints;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getPixelhinting() {
        return pixelHinting;
    }

    public void setPixelhinting(String pixelHinting) {
        this.pixelHinting = pixelHinting;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }


}