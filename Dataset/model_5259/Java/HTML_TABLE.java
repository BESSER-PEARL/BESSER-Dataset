





import java.util.List;
import java.util.ArrayList;

public class HTML_TABLE extends HTMLElement {

    private String align;
    private String width;
    private String cellspacing;
    private String bgcolor;
    private int border;
    private String cellpadding;



    public HTML_TABLE(
        String align,        String width,        String cellspacing,        String bgcolor,        int border,        String cellpadding    ) {
        super(
        );
        this.align = align;
        this.width = width;
        this.cellspacing = cellspacing;
        this.bgcolor = bgcolor;
        this.border = border;
        this.cellpadding = cellpadding;
    }


    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getCellspacing() {
        return cellspacing;
    }

    public void setCellspacing(String cellspacing) {
        this.cellspacing = cellspacing;
    }
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }
    public int getBorder() {
        return border;
    }

    public void setBorder(int border) {
        this.border = border;
    }
    public String getCellpadding() {
        return cellpadding;
    }

    public void setCellpadding(String cellpadding) {
        this.cellpadding = cellpadding;
    }


}