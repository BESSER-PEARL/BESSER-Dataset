





import java.util.List;
import java.util.ArrayList;

public class fxg_GradientGlowFilter  {

    private String quality;
    private String blurX;
    private String inner;
    private String knockout;
    private String angle;
    private String distance;
    private String blurY;
    private String strength;



    public fxg_GradientGlowFilter(
        String quality,        String blurX,        String inner,        String knockout,        String angle,        String distance,        String blurY,        String strength    ) {
        this.quality = quality;
        this.blurX = blurX;
        this.inner = inner;
        this.knockout = knockout;
        this.angle = angle;
        this.distance = distance;
        this.blurY = blurY;
        this.strength = strength;
    }


    public String getQuality() {
        return quality;
    }

    public void setQuality(String quality) {
        this.quality = quality;
    }
    public String getBlurx() {
        return blurX;
    }

    public void setBlurx(String blurX) {
        this.blurX = blurX;
    }
    public String getInner() {
        return inner;
    }

    public void setInner(String inner) {
        this.inner = inner;
    }
    public String getKnockout() {
        return knockout;
    }

    public void setKnockout(String knockout) {
        this.knockout = knockout;
    }
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
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
    public String getStrength() {
        return strength;
    }

    public void setStrength(String strength) {
        this.strength = strength;
    }


}