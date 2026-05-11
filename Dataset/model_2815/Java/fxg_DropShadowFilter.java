





import java.util.List;
import java.util.ArrayList;

public class fxg_DropShadowFilter extends Filter {

    private String blurY;
    private String strength;
    private String color;
    private String quality;
    private String angle;
    private String inner;
    private String alpha;
    private String hideObject;
    private String blurX;
    private String distance;
    private String knockout;



    public fxg_DropShadowFilter(
        String blurY,        String strength,        String color,        String quality,        String angle,        String inner,        String alpha,        String hideObject,        String blurX,        String distance,        String knockout    ) {
        super(
        );
        this.blurY = blurY;
        this.strength = strength;
        this.color = color;
        this.quality = quality;
        this.angle = angle;
        this.inner = inner;
        this.alpha = alpha;
        this.hideObject = hideObject;
        this.blurX = blurX;
        this.distance = distance;
        this.knockout = knockout;
    }


    public String getBlury() {
        return blurY;
    }

    public void setBlury(String blurY) {
        this.blurY = blurY;
    }
    public String getStrength() {
        return strength;
    }

    public void setStrength(String strength) {
        this.strength = strength;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getQuality() {
        return quality;
    }

    public void setQuality(String quality) {
        this.quality = quality;
    }
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public String getInner() {
        return inner;
    }

    public void setInner(String inner) {
        this.inner = inner;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getHideobject() {
        return hideObject;
    }

    public void setHideobject(String hideObject) {
        this.hideObject = hideObject;
    }
    public String getBlurx() {
        return blurX;
    }

    public void setBlurx(String blurX) {
        this.blurX = blurX;
    }
    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }
    public String getKnockout() {
        return knockout;
    }

    public void setKnockout(String knockout) {
        this.knockout = knockout;
    }


}