





import java.util.List;
import java.util.ArrayList;

public class model_FontAttribute  {

    private int textAlignment;
    private String font;
    private int textPosition;
    private String fontColor;



    public model_FontAttribute(
        int textAlignment,        String font,        int textPosition,        String fontColor    ) {
        this.textAlignment = textAlignment;
        this.font = font;
        this.textPosition = textPosition;
        this.fontColor = fontColor;
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