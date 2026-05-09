





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_View extends Observer {

    private String fontName;
    private String controller;
    private String fontColor;



    public AssistantMVC_View(
        String fontName,        String controller,        String fontColor    ) {
        super(
        );
        this.fontName = fontName;
        this.controller = controller;
        this.fontColor = fontColor;
    }


    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public String getController() {
        return controller;
    }

    public void setController(String controller) {
        this.controller = controller;
    }
    public String getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(String fontColor) {
        this.fontColor = fontColor;
    }


}