





import java.util.List;
import java.util.ArrayList;

public class fxg_GradientBevelFilter  {

    private String knockout;
    private String type;
    private String distance;
    private String strength;
    private String angle;
    private String blurX;
    private String blurY;
    private String quality;



    public fxg_GradientBevelFilter(
        String knockout,        String type,        String distance,        String strength,        String angle,        String blurX,        String blurY,        String quality    ) {
        this.knockout = knockout;
        this.type = type;
        this.distance = distance;
        this.strength = strength;
        this.angle = angle;
        this.blurX = blurX;
        this.blurY = blurY;
        this.quality = quality;
    }


    public String getKnockout() {
        return knockout;
    }

    public void setKnockout(String knockout) {
        this.knockout = knockout;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }
    public String getStrength() {
        return strength;
    }

    public void setStrength(String strength) {
        this.strength = strength;
    }
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public String getBlurx() {
        return blurX;
    }

    public void setBlurx(String blurX) {
        this.blurX = blurX;
    }
    public String getBlury() {
        return blurY;
    }

    public void setBlury(String blurY) {
        this.blurY = blurY;
    }
    public String getQuality() {
        return quality;
    }

    public void setQuality(String quality) {
        this.quality = quality;
    }


}