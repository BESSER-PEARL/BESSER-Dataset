





import java.util.List;
import java.util.ArrayList;

public class fxg_GradientBevelFilter  {

    private String blurY;
    private String blurX;
    private String knockout;
    private String angle;
    private String type;
    private String quality;
    private String strength;
    private String distance;



    public fxg_GradientBevelFilter(
        String blurY,        String blurX,        String knockout,        String angle,        String type,        String quality,        String strength,        String distance    ) {
        this.blurY = blurY;
        this.blurX = blurX;
        this.knockout = knockout;
        this.angle = angle;
        this.type = type;
        this.quality = quality;
        this.strength = strength;
        this.distance = distance;
    }


    public String getBlury() {
        return blurY;
    }

    public void setBlury(String blurY) {
        this.blurY = blurY;
    }
    public String getBlurx() {
        return blurX;
    }

    public void setBlurx(String blurX) {
        this.blurX = blurX;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }


}