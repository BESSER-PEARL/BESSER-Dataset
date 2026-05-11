





import java.util.List;
import java.util.ArrayList;

public class fxg_DropShadowFilter extends Filter {

    private String color;
    private String angle;
    private String knockout;
    private String quality;
    private String strength;
    private String alpha;
    private String blurX;
    private String hideObject;
    private String inner;
    private String distance;
    private String blurY;



    public fxg_DropShadowFilter(
        String color,        String angle,        String knockout,        String quality,        String strength,        String alpha,        String blurX,        String hideObject,        String inner,        String distance,        String blurY    ) {
        super(
        );
        this.color = color;
        this.angle = angle;
        this.knockout = knockout;
        this.quality = quality;
        this.strength = strength;
        this.alpha = alpha;
        this.blurX = blurX;
        this.hideObject = hideObject;
        this.inner = inner;
        this.distance = distance;
        this.blurY = blurY;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public String getKnockout() {
        return knockout;
    }

    public void setKnockout(String knockout) {
        this.knockout = knockout;
    }
    public String getQuality() {
        return quality;
    }

    public void setQuality(String quality) {
        this.quality = quality;
    }
    public String getStrength() {
        return strength;
    }

    public void setStrength(String strength) {
        this.strength = strength;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getBlurx() {
        return blurX;
    }

    public void setBlurx(String blurX) {
        this.blurX = blurX;
    }
    public String getHideobject() {
        return hideObject;
    }

    public void setHideobject(String hideObject) {
        this.hideObject = hideObject;
    }
    public String getInner() {
        return inner;
    }

    public void setInner(String inner) {
        this.inner = inner;
    }
    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }
    public String getBlury() {
        return blurY;
    }

    public void setBlury(String blurY) {
        this.blurY = blurY;
    }


}