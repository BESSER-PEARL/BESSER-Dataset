





import java.util.List;
import java.util.ArrayList;

public class notation_FontStyle extends Style {

    private String fontName;
    private boolean strikeThrough;
    private boolean underline;
    private int fontColor;
    private boolean bold;
    private int fontHeight;
    private boolean italic;



    public notation_FontStyle(
        String fontName,        boolean strikeThrough,        boolean underline,        int fontColor,        boolean bold,        int fontHeight,        boolean italic    ) {
        super(
        );
        this.fontName = fontName;
        this.strikeThrough = strikeThrough;
        this.underline = underline;
        this.fontColor = fontColor;
        this.bold = bold;
        this.fontHeight = fontHeight;
        this.italic = italic;
    }


    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public boolean getStrikethrough() {
        return strikeThrough;
    }

    public void setStrikethrough(boolean strikeThrough) {
        this.strikeThrough = strikeThrough;
    }
    public boolean getUnderline() {
        return underline;
    }

    public void setUnderline(boolean underline) {
        this.underline = underline;
    }
    public int getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(int fontColor) {
        this.fontColor = fontColor;
    }
    public boolean getBold() {
        return bold;
    }

    public void setBold(boolean bold) {
        this.bold = bold;
    }
    public int getFontheight() {
        return fontHeight;
    }

    public void setFontheight(int fontHeight) {
        this.fontHeight = fontHeight;
    }
    public boolean getItalic() {
        return italic;
    }

    public void setItalic(boolean italic) {
        this.italic = italic;
    }


}