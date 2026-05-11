





import java.util.List;
import java.util.ArrayList;

public class fxg_BevelFilter extends Filter {

    private String blurY;
    private String strength;
    private String knockout;
    private String distance;
    private String highlightAlpha;
    private String highlightColor;
    private String blurX;
    private String shadowColor;
    private String quality;
    private String type;
    private String angle;
    private String shadowAlpha;



    public fxg_BevelFilter(
        String blurY,        String strength,        String knockout,        String distance,        String highlightAlpha,        String highlightColor,        String blurX,        String shadowColor,        String quality,        String type,        String angle,        String shadowAlpha    ) {
        super(
        );
        this.blurY = blurY;
        this.strength = strength;
        this.knockout = knockout;
        this.distance = distance;
        this.highlightAlpha = highlightAlpha;
        this.highlightColor = highlightColor;
        this.blurX = blurX;
        this.shadowColor = shadowColor;
        this.quality = quality;
        this.type = type;
        this.angle = angle;
        this.shadowAlpha = shadowAlpha;
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
    public String getKnockout() {
        return knockout;
    }

    public void setKnockout(String knockout) {
        this.knockout = knockout;
    }
    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }
    public String getHighlightalpha() {
        return highlightAlpha;
    }

    public void setHighlightalpha(String highlightAlpha) {
        this.highlightAlpha = highlightAlpha;
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
    public String getShadowcolor() {
        return shadowColor;
    }

    public void setShadowcolor(String shadowColor) {
        this.shadowColor = shadowColor;
    }
    public String getQuality() {
        return quality;
    }

    public void setQuality(String quality) {
        this.quality = quality;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAngle() {
        return angle;
    }

    public void setAngle(String angle) {
        this.angle = angle;
    }
    public String getShadowalpha() {
        return shadowAlpha;
    }

    public void setShadowalpha(String shadowAlpha) {
        this.shadowAlpha = shadowAlpha;
    }


}