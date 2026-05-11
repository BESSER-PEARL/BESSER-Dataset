





import java.util.List;
import java.util.ArrayList;

public class diastyle_DNodeEdgeStyle extends DBaseStyle, EModelElement {

    private String line;
    private String fontName;
    private int fontSize;
    private int lineWidth;
    private String fontColor;
    private String textAlignment;
    private String fontStyle;
    private String icon;



    public diastyle_DNodeEdgeStyle(
        String line,        String fontName,        int fontSize,        int lineWidth,        String fontColor,        String textAlignment,        String fontStyle,        String icon    ) {
        super(
        );
        this.line = line;
        this.fontName = fontName;
        this.fontSize = fontSize;
        this.lineWidth = lineWidth;
        this.fontColor = fontColor;
        this.textAlignment = textAlignment;
        this.fontStyle = fontStyle;
        this.icon = icon;
    }


    public String getLine() {
        return line;
    }

    public void setLine(String line) {
        this.line = line;
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
    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public String getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(String fontColor) {
        this.fontColor = fontColor;
    }
    public String getTextalignment() {
        return textAlignment;
    }

    public void setTextalignment(String textAlignment) {
        this.textAlignment = textAlignment;
    }
    public String getFontstyle() {
        return fontStyle;
    }

    public void setFontstyle(String fontStyle) {
        this.fontStyle = fontStyle;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }


}