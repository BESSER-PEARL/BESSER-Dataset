





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_FontType  {

    private String verticalAlign;
    private String underline;
    private String bold;
    private String outline;
    private String shadow;
    private String fontName;
    private String size;
    private String color;
    private String italic;
    private String strikeThrough;





    private StyleType styletype;


    public SpreadsheetMLStyles_FontType(
        String verticalAlign,        String underline,        String bold,        String outline,        String shadow,        String fontName,        String size,        String color,        String italic,        String strikeThrough    ) {
        this.verticalAlign = verticalAlign;
        this.underline = underline;
        this.bold = bold;
        this.outline = outline;
        this.shadow = shadow;
        this.fontName = fontName;
        this.size = size;
        this.color = color;
        this.italic = italic;
        this.strikeThrough = strikeThrough;
    }


    public String getVerticalalign() {
        return verticalAlign;
    }

    public void setVerticalalign(String verticalAlign) {
        this.verticalAlign = verticalAlign;
    }
    public String getUnderline() {
        return underline;
    }

    public void setUnderline(String underline) {
        this.underline = underline;
    }
    public String getBold() {
        return bold;
    }

    public void setBold(String bold) {
        this.bold = bold;
    }
    public String getOutline() {
        return outline;
    }

    public void setOutline(String outline) {
        this.outline = outline;
    }
    public String getShadow() {
        return shadow;
    }

    public void setShadow(String shadow) {
        this.shadow = shadow;
    }
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getItalic() {
        return italic;
    }

    public void setItalic(String italic) {
        this.italic = italic;
    }
    public String getStrikethrough() {
        return strikeThrough;
    }

    public void setStrikethrough(String strikeThrough) {
        this.strikeThrough = strikeThrough;
    }

    public StyleType getStyletype() {
        return styletype;
    }

    public void setStyletype(StyleType styletype) {
        this.styletype = styletype;
    }

}