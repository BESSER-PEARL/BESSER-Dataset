





import java.util.List;
import java.util.ArrayList;

public class fxg_SolidColorStroke extends Stroke {

    private String alpha;
    private String color;
    private String pixelHinting;
    private String weight;
    private String scaleMode;
    private String joints;
    private String miterLimit;
    private String caps;



    public fxg_SolidColorStroke(
        String alpha,        String color,        String pixelHinting,        String weight,        String scaleMode,        String joints,        String miterLimit,        String caps    ) {
        super(
        );
        this.alpha = alpha;
        this.color = color;
        this.pixelHinting = pixelHinting;
        this.weight = weight;
        this.scaleMode = scaleMode;
        this.joints = joints;
        this.miterLimit = miterLimit;
        this.caps = caps;
    }


    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
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


}