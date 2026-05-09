





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_View extends Observer {

    private String fontName;
    private String fontColor;



    public AssistantMVC_View(
        String fontName,        String fontColor    ) {
        super(
        );
        this.fontName = fontName;
        this.fontColor = fontColor;
    }


    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public String getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(String fontColor) {
        this.fontColor = fontColor;
    }


}