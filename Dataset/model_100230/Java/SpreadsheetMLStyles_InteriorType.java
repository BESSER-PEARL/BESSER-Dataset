





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_InteriorType  {

    private String patternColor;
    private String pattern;
    private String color;





    private StyleType styletype;


    public SpreadsheetMLStyles_InteriorType(
        String patternColor,        String pattern,        String color    ) {
        this.patternColor = patternColor;
        this.pattern = pattern;
        this.color = color;
    }


    public String getPatterncolor() {
        return patternColor;
    }

    public void setPatterncolor(String patternColor) {
        this.patternColor = patternColor;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public StyleType getStyletype() {
        return styletype;
    }

    public void setStyletype(StyleType styletype) {
        this.styletype = styletype;
    }

}