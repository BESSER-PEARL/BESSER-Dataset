





import java.util.List;
import java.util.ArrayList;

public class notation_FontStyle extends Style {

    private boolean italic;
    private String fontName;
    private int fontHeight;
    private boolean bold;
    private boolean strikeThrough;
    private boolean underline;
    private int fontColor;



    public notation_FontStyle(
        boolean italic,        String fontName,        int fontHeight,        boolean bold,        boolean strikeThrough,        boolean underline,        int fontColor    ) {
        super(
        );
        this.italic = italic;
        this.fontName = fontName;
        this.fontHeight = fontHeight;
        this.bold = bold;
        this.strikeThrough = strikeThrough;
        this.underline = underline;
        this.fontColor = fontColor;
    }


    public boolean getItalic() {
        return italic;
    }

    public void setItalic(boolean italic) {
        this.italic = italic;
    }
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public int getFontheight() {
        return fontHeight;
    }

    public void setFontheight(int fontHeight) {
        this.fontHeight = fontHeight;
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


}