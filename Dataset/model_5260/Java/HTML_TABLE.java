





import java.util.List;
import java.util.ArrayList;

public class HTML_TABLE extends HTMLElement {

    private String cellpadding;
    private String bgcolor;
    private String align;
    private String cellspacing;
    private int border;
    private String width;



    public HTML_TABLE(
        String cellpadding,        String bgcolor,        String align,        String cellspacing,        int border,        String width    ) {
        super(
        );
        this.cellpadding = cellpadding;
        this.bgcolor = bgcolor;
        this.align = align;
        this.cellspacing = cellspacing;
        this.border = border;
        this.width = width;
    }


    public String getCellpadding() {
        return cellpadding;
    }

    public void setCellpadding(String cellpadding) {
        this.cellpadding = cellpadding;
    }
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getCellspacing() {
        return cellspacing;
    }

    public void setCellspacing(String cellspacing) {
        this.cellspacing = cellspacing;
    }
    public int getBorder() {
        return border;
    }

    public void setBorder(int border) {
        this.border = border;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}