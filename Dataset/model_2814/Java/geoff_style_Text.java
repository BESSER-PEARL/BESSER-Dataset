





import java.util.List;
import java.util.ArrayList;

public class geoff_style_Text extends Identifiable {

    private String font;
    private String rotation;
    private float offsetX;
    private String scale;
    private String text;
    private float offsetY;
    private String textBaseLine;
    private String textAlign;



    public geoff_style_Text(
        String font,        String rotation,        float offsetX,        String scale,        String text,        float offsetY,        String textBaseLine,        String textAlign    ) {
        super(
        );
        this.font = font;
        this.rotation = rotation;
        this.offsetX = offsetX;
        this.scale = scale;
        this.text = text;
        this.offsetY = offsetY;
        this.textBaseLine = textBaseLine;
        this.textAlign = textAlign;
    }


    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public float getOffsetx() {
        return offsetX;
    }

    public void setOffsetx(float offsetX) {
        this.offsetX = offsetX;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public float getOffsety() {
        return offsetY;
    }

    public void setOffsety(float offsetY) {
        this.offsetY = offsetY;
    }
    public String getTextbaseline() {
        return textBaseLine;
    }

    public void setTextbaseline(String textBaseLine) {
        this.textBaseLine = textBaseLine;
    }
    public String getTextalign() {
        return textAlign;
    }

    public void setTextalign(String textAlign) {
        this.textAlign = textAlign;
    }


}