





import java.util.List;
import java.util.ArrayList;

public class fxg_BevelFilter extends Filter {

    private String angle;
    private String shadowColor;
    private String knockout;
    private String strength;
    private String blurY;
    private String distance;
    private String highlightColor;
    private String blurX;
    private String quality;
    private String highlightAlpha;
    private String shadowAlpha;
    private String type;



    public fxg_BevelFilter(
        String angle,        String shadowColor,        String knockout,        String strength,        String blurY,        String distance,        String highlightColor,        String blurX,        String quality,        String highlightAlpha,        String shadowAlpha,        String type    ) {
        super(
        );
        this.angle = angle;
        this.shadowColor = shadowColor;
        this.knockout = knockout;
        this.strength = strength;
        this.blurY = blurY;
        this.distance = distance;
        this.highlightColor = highlightColor;
        this.blurX = blurX;
        this.quality = quality;
        this.highlightAlpha = highlightAlpha;
        this.shadowAlpha = shadowAlpha;
        this.type = type;
    }


    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public String getShadowcolor() {
        return shadowColor;
    }

    public void setShadowcolor(String shadowColor) {
        this.shadowColor = shadowColor;
    }
    public String getKnockout() {
        return knockout;
    }

    public void setKnockout(String knockout) {
        this.knockout = knockout;
    }
    public String getStrength() {
        return strength;
    }

    public void setStrength(String strength) {
        this.strength = strength;
    }
    public String getBlury() {
        return blurY;
    }

    public void setBlury(String blurY) {
        this.blurY = blurY;
    }
    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }
    public String getHighlightcolor() {
        return highlightColor;
    }

    public void setHighlightcolor(String highlightColor) {
        this.highlightColor = highlightColor;
    }
    public String getBlurx() {
        return blurX;
    }

    public void setBlurx(String blurX) {
        this.blurX = blurX;
    }
    public String getQuality() {
        return quality;
    }

    public void setQuality(String quality) {
        this.quality = quality;
    }
    public String getHighlightalpha() {
        return highlightAlpha;
    }

    public void setHighlightalpha(String highlightAlpha) {
        this.highlightAlpha = highlightAlpha;
    }
    public String getShadowalpha() {
        return shadowAlpha;
    }

    public void setShadowalpha(String shadowAlpha) {
        this.shadowAlpha = shadowAlpha;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}