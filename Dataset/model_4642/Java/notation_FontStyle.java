





import java.util.List;
import java.util.ArrayList;

public class notation_FontStyle extends Style {

    private String fontName;
    private boolean underline;
    private int fontHeight;
    private boolean italic;
    private int fontColor;
    private boolean bold;
    private boolean strikeThrough;



    public notation_FontStyle(
        String fontName,        boolean underline,        int fontHeight,        boolean italic,        int fontColor,        boolean bold,        boolean strikeThrough    ) {
        super(
        );
        this.fontName = fontName;
        this.underline = underline;
        this.fontHeight = fontHeight;
        this.italic = italic;
        this.fontColor = fontColor;
        this.bold = bold;
        this.strikeThrough = strikeThrough;
    }


    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public boolean getUnderline() {
        return underline;
    }

    public void setUnderline(boolean underline) {
        this.underline = underline;
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
    public boolean getStrikethrough() {
        return strikeThrough;
    }

    public void setStrikethrough(boolean strikeThrough) {
        this.strikeThrough = strikeThrough;
    }


}