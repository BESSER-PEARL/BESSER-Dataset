





import java.util.List;
import java.util.ArrayList;

public class model_FontAttribute  {

    private String fontColor;
    private int textAlignment;
    private int textPosition;
    private String font;



    public model_FontAttribute(
        String fontColor,        int textAlignment,        int textPosition,        String font    ) {
        this.fontColor = fontColor;
        this.textAlignment = textAlignment;
        this.textPosition = textPosition;
        this.font = font;
    }


    public String getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(String fontColor) {
        this.fontColor = fontColor;
    }
    public int getTextalignment() {
        return textAlignment;
    }

    public void setTextalignment(int textAlignment) {
        this.textAlignment = textAlignment;
    }
    public int getTextposition() {
        return textPosition;
    }

    public void setTextposition(int textPosition) {
        this.textPosition = textPosition;
    }
    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }


}