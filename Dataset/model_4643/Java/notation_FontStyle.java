





import java.util.List;
import java.util.ArrayList;

public class notation_FontStyle extends Style {

    private int fontHeight;
    private boolean bold;
    private boolean underline;
    private boolean italic;
    private boolean strikeThrough;
    private int fontColor;
    private String fontName;



    public notation_FontStyle(
        int fontHeight,        boolean bold,        boolean underline,        boolean italic,        boolean strikeThrough,        int fontColor,        String fontName    ) {
        super(
        );
        this.fontHeight = fontHeight;
        this.bold = bold;
        this.underline = underline;
        this.italic = italic;
        this.strikeThrough = strikeThrough;
        this.fontColor = fontColor;
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
    public boolean getUnderline() {
        return underline;
    }

    public void setUnderline(boolean underline) {
        this.underline = underline;
    }
    public boolean getItalic() {
        return italic;
    }

    public void setItalic(boolean italic) {
        this.italic = italic;
    }
    public boolean getStrikethrough() {
        return strikeThrough;
    }

    public void setStrikethrough(boolean strikeThrough) {
        this.strikeThrough = strikeThrough;
    }
    public int getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(int fontColor) {
        this.fontColor = fontColor;
    }
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }


}