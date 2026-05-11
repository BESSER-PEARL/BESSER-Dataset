





import java.util.List;
import java.util.ArrayList;

public class model_FontAttribute  {

    private String font;
    private int textPosition;
    private int textAlignment;
    private String fontColor;



    public model_FontAttribute(
        String font,        int textPosition,        int textAlignment,        String fontColor    ) {
        this.font = font;
        this.textPosition = textPosition;
        this.textAlignment = textAlignment;
        this.fontColor = fontColor;
    }


    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }
    public int getTextposition() {
        return textPosition;
    }

    public void setTextposition(int textPosition) {
        this.textPosition = textPosition;
    }
    public int getTextalignment() {
        return textAlignment;
    }

    public void setTextalignment(int textAlignment) {
        this.textAlignment = textAlignment;
    }
    public String getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(String fontColor) {
        this.fontColor = fontColor;
    }


}