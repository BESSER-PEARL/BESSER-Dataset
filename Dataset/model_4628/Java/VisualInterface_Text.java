





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Text extends Figure {

    private boolean fontBold;
    private String text;
    private String textPlacement;
    private String iconAlignment;
    private boolean fontItalic;
    private String labelAlignment;
    private int fontSize;
    private String textAlignment;
    private String fontName;



    public VisualInterface_Text(
        boolean fontBold,        String text,        String textPlacement,        String iconAlignment,        boolean fontItalic,        String labelAlignment,        int fontSize,        String textAlignment,        String fontName    ) {
        super(
        );
        this.fontBold = fontBold;
        this.text = text;
        this.textPlacement = textPlacement;
        this.iconAlignment = iconAlignment;
        this.fontItalic = fontItalic;
        this.labelAlignment = labelAlignment;
        this.fontSize = fontSize;
        this.textAlignment = textAlignment;
        this.fontName = fontName;
    }


    public boolean getFontbold() {
        return fontBold;
    }

    public void setFontbold(boolean fontBold) {
        this.fontBold = fontBold;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getTextplacement() {
        return textPlacement;
    }

    public void setTextplacement(String textPlacement) {
        this.textPlacement = textPlacement;
    }
    public String getIconalignment() {
        return iconAlignment;
    }

    public void setIconalignment(String iconAlignment) {
        this.iconAlignment = iconAlignment;
    }
    public boolean getFontitalic() {
        return fontItalic;
    }

    public void setFontitalic(boolean fontItalic) {
        this.fontItalic = fontItalic;
    }
    public String getLabelalignment() {
        return labelAlignment;
    }

    public void setLabelalignment(String labelAlignment) {
        this.labelAlignment = labelAlignment;
    }
    public int getFontsize() {
        return fontSize;
    }

    public void setFontsize(int fontSize) {
        this.fontSize = fontSize;
    }
    public String getTextalignment() {
        return textAlignment;
    }

    public void setTextalignment(String textAlignment) {
        this.textAlignment = textAlignment;
    }
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }


}