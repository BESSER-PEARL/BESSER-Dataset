





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Text extends Figure {

    private String labelAlignment;
    private String iconAlignment;
    private String text;
    private String fontName;
    private String textAlignment;
    private boolean fontItalic;
    private boolean fontBold;
    private int fontSize;
    private String textPlacement;



    public VisualInterface_Text(
        String labelAlignment,        String iconAlignment,        String text,        String fontName,        String textAlignment,        boolean fontItalic,        boolean fontBold,        int fontSize,        String textPlacement    ) {
        super(
        );
        this.labelAlignment = labelAlignment;
        this.iconAlignment = iconAlignment;
        this.text = text;
        this.fontName = fontName;
        this.textAlignment = textAlignment;
        this.fontItalic = fontItalic;
        this.fontBold = fontBold;
        this.fontSize = fontSize;
        this.textPlacement = textPlacement;
    }


    public String getLabelalignment() {
        return labelAlignment;
    }

    public void setLabelalignment(String labelAlignment) {
        this.labelAlignment = labelAlignment;
    }
    public String getIconalignment() {
        return iconAlignment;
    }

    public void setIconalignment(String iconAlignment) {
        this.iconAlignment = iconAlignment;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public String getTextalignment() {
        return textAlignment;
    }

    public void setTextalignment(String textAlignment) {
        this.textAlignment = textAlignment;
    }
    public boolean getFontitalic() {
        return fontItalic;
    }

    public void setFontitalic(boolean fontItalic) {
        this.fontItalic = fontItalic;
    }
    public boolean getFontbold() {
        return fontBold;
    }

    public void setFontbold(boolean fontBold) {
        this.fontBold = fontBold;
    }
    public int getFontsize() {
        return fontSize;
    }

    public void setFontsize(int fontSize) {
        this.fontSize = fontSize;
    }
    public String getTextplacement() {
        return textPlacement;
    }

    public void setTextplacement(String textPlacement) {
        this.textPlacement = textPlacement;
    }


}