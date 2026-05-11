





import java.util.List;
import java.util.ArrayList;

public class fxg_GradientGlowFilter  {

    private String angle;
    private String strength;
    private String blurX;
    private String distance;
    private String knockout;
    private String quality;
    private String blurY;
    private String inner;



    public fxg_GradientGlowFilter(
        String angle,        String strength,        String blurX,        String distance,        String knockout,        String quality,        String blurY,        String inner    ) {
        this.angle = angle;
        this.strength = strength;
        this.blurX = blurX;
        this.distance = distance;
        this.knockout = knockout;
        this.quality = quality;
        this.blurY = blurY;
        this.inner = inner;
    }


    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public String getStrength() {
        return strength;
    }

    public void setStrength(String strength) {
        this.strength = strength;
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
    public String getQuality() {
        return quality;
    }

    public void setQuality(String quality) {
        this.quality = quality;
    }
    public String getBlury() {
        return blurY;
    }

    public void setBlury(String blurY) {
        this.blurY = blurY;
    }
    public String getInner() {
        return inner;
    }

    public void setInner(String inner) {
        this.inner = inner;
    }


}