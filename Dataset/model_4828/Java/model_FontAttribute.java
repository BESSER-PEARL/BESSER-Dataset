





import java.util.List;
import java.util.ArrayList;

public class model_FontAttribute  {

    private String fontColor;
    private String font;



    public model_FontAttribute(
        String fontColor,        String font    ) {
        this.fontColor = fontColor;
        this.font = font;
    }


    public String getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(String fontColor) {
        this.fontColor = fontColor;
    }
    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }


}