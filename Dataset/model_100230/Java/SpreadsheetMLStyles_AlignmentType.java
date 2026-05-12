





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_AlignmentType  {

    private String rotate;
    private String verticalText;
    private String readingOrder;
    private String indent;
    private String wrapText;
    private String horizontal;
    private String vertical;
    private String shrinkToFit;





    private StyleType styletype;


    public SpreadsheetMLStyles_AlignmentType(
        String rotate,        String verticalText,        String readingOrder,        String indent,        String wrapText,        String horizontal,        String vertical,        String shrinkToFit    ) {
        this.rotate = rotate;
        this.verticalText = verticalText;
        this.readingOrder = readingOrder;
        this.indent = indent;
        this.wrapText = wrapText;
        this.horizontal = horizontal;
        this.vertical = vertical;
        this.shrinkToFit = shrinkToFit;
    }


    public String getRotate() {
        return rotate;
    }

    public void setRotate(String rotate) {
        this.rotate = rotate;
    }
    public String getVerticaltext() {
        return verticalText;
    }

    public void setVerticaltext(String verticalText) {
        this.verticalText = verticalText;
    }
    public String getReadingorder() {
        return readingOrder;
    }

    public void setReadingorder(String readingOrder) {
        this.readingOrder = readingOrder;
    }
    public String getIndent() {
        return indent;
    }

    public void setIndent(String indent) {
        this.indent = indent;
    }
    public String getWraptext() {
        return wrapText;
    }

    public void setWraptext(String wrapText) {
        this.wrapText = wrapText;
    }
    public String getHorizontal() {
        return horizontal;
    }

    public void setHorizontal(String horizontal) {
        this.horizontal = horizontal;
    }
    public String getVertical() {
        return vertical;
    }

    public void setVertical(String vertical) {
        this.vertical = vertical;
    }
    public String getShrinktofit() {
        return shrinkToFit;
    }

    public void setShrinktofit(String shrinkToFit) {
        this.shrinkToFit = shrinkToFit;
    }

    public StyleType getStyletype() {
        return styletype;
    }

    public void setStyletype(StyleType styletype) {
        this.styletype = styletype;
    }

}