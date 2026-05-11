





import java.util.List;
import java.util.ArrayList;

public class model_FontAttribute  {

    private String font;
    private int textAlignment;
    private int textPosition;
    private String fontColor;



    public model_FontAttribute(
        String font,        int textAlignment,        int textPosition,        String fontColor    ) {
        this.font = font;
        this.textAlignment = textAlignment;
        this.textPosition = textPosition;
        this.fontColor = fontColor;
    }


    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
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
    public String getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(String fontColor) {
        this.fontColor = fontColor;
    }


}