





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_View extends Observer {

    private String fontColor;
    private String fontName;



    public AssistantMVC_View(
        String fontColor,        String fontName    ) {
        super(
        );
        this.fontColor = fontColor;
        this.fontName = fontName;
    }


    public String getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(String fontColor) {
        this.fontColor = fontColor;
    }
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }


}