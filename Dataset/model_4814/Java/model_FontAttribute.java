





import java.util.List;
import java.util.ArrayList;

public class model_FontAttribute  {

    private int textPosition;
    private int textAlignment;
    private String font;
    private String fontColor;



    public model_FontAttribute(
        int textPosition,        int textAlignment,        String font,        String fontColor    ) {
        this.textPosition = textPosition;
        this.textAlignment = textAlignment;
        this.font = font;
        this.fontColor = fontColor;
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
    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }
    public String getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(String fontColor) {
        this.fontColor = fontColor;
    }


}