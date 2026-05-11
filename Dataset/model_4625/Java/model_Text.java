





import java.util.List;
import java.util.ArrayList;

public class model_Text extends Figure {

    private String textAlignment;
    private String alpha;
    private String labelAlignment;
    private boolean fontBold;
    private String text;
    private boolean fontItalic;
    private String iconAlignment;
    private int fontSize;
    private String textPlacement;
    private String fontName;



    public model_Text(
        String textAlignment,        String alpha,        String labelAlignment,        boolean fontBold,        String text,        boolean fontItalic,        String iconAlignment,        int fontSize,        String textPlacement,        String fontName    ) {
        super(
        );
        this.textAlignment = textAlignment;
        this.alpha = alpha;
        this.labelAlignment = labelAlignment;
        this.fontBold = fontBold;
        this.text = text;
        this.fontItalic = fontItalic;
        this.iconAlignment = iconAlignment;
        this.fontSize = fontSize;
        this.textPlacement = textPlacement;
        this.fontName = fontName;
    }


    public String getTextalignment() {
        return textAlignment;
    }

    public void setTextalignment(String textAlignment) {
        this.textAlignment = textAlignment;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
    }
    public String getLabelalignment() {
        return labelAlignment;
    }

    public void setLabelalignment(String labelAlignment) {
        this.labelAlignment = labelAlignment;
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
    public boolean getFontitalic() {
        return fontItalic;
    }

    public void setFontitalic(boolean fontItalic) {
        this.fontItalic = fontItalic;
    }
    public String getIconalignment() {
        return iconAlignment;
    }

    public void setIconalignment(String iconAlignment) {
        this.iconAlignment = iconAlignment;
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
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }


}