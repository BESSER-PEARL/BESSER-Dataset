





import java.util.List;
import java.util.ArrayList;

public class notation_FontStyle extends Style {

    private boolean bold;
    private boolean underline;
    private int fontColor;
    private boolean strikeThrough;
    private int fontHeight;
    private boolean italic;
    private String fontName;



    public notation_FontStyle(
        boolean bold,        boolean underline,        int fontColor,        boolean strikeThrough,        int fontHeight,        boolean italic,        String fontName    ) {
        super(
        );
        this.bold = bold;
        this.underline = underline;
        this.fontColor = fontColor;
        this.strikeThrough = strikeThrough;
        this.fontHeight = fontHeight;
        this.italic = italic;
        this.fontName = fontName;
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
    public int getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(int fontColor) {
        this.fontColor = fontColor;
    }
    public boolean getStrikethrough() {
        return strikeThrough;
    }

    public void setStrikethrough(boolean strikeThrough) {
        this.strikeThrough = strikeThrough;
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
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }


}