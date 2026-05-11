





import java.util.List;
import java.util.ArrayList;

public class notation_FontStyle extends Style {

    private boolean underline;
    private boolean strikeThrough;
    private String fontName;
    private boolean bold;
    private boolean italic;
    private int fontColor;
    private int fontHeight;



    public notation_FontStyle(
        boolean underline,        boolean strikeThrough,        String fontName,        boolean bold,        boolean italic,        int fontColor,        int fontHeight    ) {
        super(
        );
        this.underline = underline;
        this.strikeThrough = strikeThrough;
        this.fontName = fontName;
        this.bold = bold;
        this.italic = italic;
        this.fontColor = fontColor;
        this.fontHeight = fontHeight;
    }


    public boolean getUnderline() {
        return underline;
    }

    public void setUnderline(boolean underline) {
        this.underline = underline;
    }
    public boolean getStrikethrough() {
        return strikeThrough;
    }

    public void setStrikethrough(boolean strikeThrough) {
        this.strikeThrough = strikeThrough;
    }
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public boolean getBold() {
        return bold;
    }

    public void setBold(boolean bold) {
        this.bold = bold;
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
    public int getFontheight() {
        return fontHeight;
    }

    public void setFontheight(int fontHeight) {
        this.fontHeight = fontHeight;
    }


}