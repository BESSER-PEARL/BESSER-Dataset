





import java.util.List;
import java.util.ArrayList;

public class model_Text extends Figure {

    private String labelAlignment;
    private String iconAlignment;
    private boolean fontBold;
    private String fontName;
    private String text;
    private int fontSize;
    private String textPlacement;
    private boolean fontItalic;
    private String textAlignment;



    public model_Text(
        String labelAlignment,        String iconAlignment,        boolean fontBold,        String fontName,        String text,        int fontSize,        String textPlacement,        boolean fontItalic,        String textAlignment    ) {
        super(
        );
        this.labelAlignment = labelAlignment;
        this.iconAlignment = iconAlignment;
        this.fontBold = fontBold;
        this.fontName = fontName;
        this.text = text;
        this.fontSize = fontSize;
        this.textPlacement = textPlacement;
        this.fontItalic = fontItalic;
        this.textAlignment = textAlignment;
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
    public boolean getFontbold() {
        return fontBold;
    }

    public void setFontbold(boolean fontBold) {
        this.fontBold = fontBold;
    }
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
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
    public boolean getFontitalic() {
        return fontItalic;
    }

    public void setFontitalic(boolean fontItalic) {
        this.fontItalic = fontItalic;
    }
    public String getTextalignment() {
        return textAlignment;
    }

    public void setTextalignment(String textAlignment) {
        this.textAlignment = textAlignment;
    }


}