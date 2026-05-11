





import java.util.List;
import java.util.ArrayList;

public class model_Text extends Figure {

    private String iconAlignment;
    private boolean fontItalic;
    private String fontName;
    private int fontSize;
    private String textPlacement;
    private String textAlignment;
    private String labelAlignment;
    private String alpha;
    private boolean fontBold;
    private String text;



    public model_Text(
        String iconAlignment,        boolean fontItalic,        String fontName,        int fontSize,        String textPlacement,        String textAlignment,        String labelAlignment,        String alpha,        boolean fontBold,        String text    ) {
        super(
        );
        this.iconAlignment = iconAlignment;
        this.fontItalic = fontItalic;
        this.fontName = fontName;
        this.fontSize = fontSize;
        this.textPlacement = textPlacement;
        this.textAlignment = textAlignment;
        this.labelAlignment = labelAlignment;
        this.alpha = alpha;
        this.fontBold = fontBold;
        this.text = text;
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
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
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
    public String getTextalignment() {
        return textAlignment;
    }

    public void setTextalignment(String textAlignment) {
        this.textAlignment = textAlignment;
    }
    public String getLabelalignment() {
        return labelAlignment;
    }

    public void setLabelalignment(String labelAlignment) {
        this.labelAlignment = labelAlignment;
    }
    public String getAlpha() {
        return alpha;
    }

    public void setAlpha(String alpha) {
        this.alpha = alpha;
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


}