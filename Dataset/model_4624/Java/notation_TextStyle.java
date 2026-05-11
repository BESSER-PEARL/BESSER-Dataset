





import java.util.List;
import java.util.ArrayList;

public class notation_TextStyle extends Style {

    private String fontColor;
    private boolean bold;
    private int fontSize;
    private boolean underlined;
    private String fontName;
    private boolean italic;





    private notation_Label notation_label;


    public notation_TextStyle(
        String fontColor,        boolean bold,        int fontSize,        boolean underlined,        String fontName,        boolean italic    ) {
        super(
        );
        this.fontColor = fontColor;
        this.bold = bold;
        this.fontSize = fontSize;
        this.underlined = underlined;
        this.fontName = fontName;
        this.italic = italic;
    }


    public String getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(String fontColor) {
        this.fontColor = fontColor;
    }
    public boolean getBold() {
        return bold;
    }

    public void setBold(boolean bold) {
        this.bold = bold;
    }
    public int getFontsize() {
        return fontSize;
    }

    public void setFontsize(int fontSize) {
        this.fontSize = fontSize;
    }
    public boolean getUnderlined() {
        return underlined;
    }

    public void setUnderlined(boolean underlined) {
        this.underlined = underlined;
    }
    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public boolean getItalic() {
        return italic;
    }

    public void setItalic(boolean italic) {
        this.italic = italic;
    }

    public notation_Label getNotation_label() {
        return notation_label;
    }

    public void setNotation_label(notation_Label notation_label) {
        this.notation_label = notation_label;
    }

}