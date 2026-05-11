





import java.util.List;
import java.util.ArrayList;

public class notation_FontStyle extends Style {

    private boolean italic;
    private boolean bold;
    private boolean underline;
    private int fontHeight;
    private boolean strikeThrough;
    private int fontColor;
    private String fontName;



    public notation_FontStyle(
        boolean italic,        boolean bold,        boolean underline,        int fontHeight,        boolean strikeThrough,        int fontColor,        String fontName    ) {
        super(
        );
        this.italic = italic;
        this.bold = bold;
        this.underline = underline;
        this.fontHeight = fontHeight;
        this.strikeThrough = strikeThrough;
        this.fontColor = fontColor;
        this.fontName = fontName;
    }


    public boolean getItalic() {
        return italic;
    }

    public void setItalic(boolean italic) {
        this.italic = italic;
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
    public int getFontheight() {
        return fontHeight;
    }

    public void setFontheight(int fontHeight) {
        this.fontHeight = fontHeight;
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