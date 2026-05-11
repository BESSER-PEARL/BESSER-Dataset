





import java.util.List;
import java.util.ArrayList;

public class cevinedit_Link extends PersonalizedElement {

    private int width;
    private String brightness;
    private String sourceDecoration;
    private String targetDecoration;
    private String label;
    private String texture;
    private String color;
    private String labelFontStyle;



    public cevinedit_Link(
        int width,        String brightness,        String sourceDecoration,        String targetDecoration,        String label,        String texture,        String color,        String labelFontStyle    ) {
        super(
        );
        this.width = width;
        this.brightness = brightness;
        this.sourceDecoration = sourceDecoration;
        this.targetDecoration = targetDecoration;
        this.label = label;
        this.texture = texture;
        this.color = color;
        this.labelFontStyle = labelFontStyle;
    }


    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getBrightness() {
        return brightness;
    }

    public void setBrightness(String brightness) {
        this.brightness = brightness;
    }
    public String getSourcedecoration() {
        return sourceDecoration;
    }

    public void setSourcedecoration(String sourceDecoration) {
        this.sourceDecoration = sourceDecoration;
    }
    public String getTargetdecoration() {
        return targetDecoration;
    }

    public void setTargetdecoration(String targetDecoration) {
        this.targetDecoration = targetDecoration;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getTexture() {
        return texture;
    }

    public void setTexture(String texture) {
        this.texture = texture;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getLabelfontstyle() {
        return labelFontStyle;
    }

    public void setLabelfontstyle(String labelFontStyle) {
        this.labelFontStyle = labelFontStyle;
    }


}