





import java.util.List;
import java.util.ArrayList;

public class HTML_TD extends HTMLElement {

    private String rowspan;
    private String height;
    private String align;
    private String bgcolor;
    private String colspan;
    private String valign;
    private String width;



    public HTML_TD(
        String rowspan,        String height,        String align,        String bgcolor,        String colspan,        String valign,        String width    ) {
        super(
        );
        this.rowspan = rowspan;
        this.height = height;
        this.align = align;
        this.bgcolor = bgcolor;
        this.colspan = colspan;
        this.valign = valign;
        this.width = width;
    }


    public String getRowspan() {
        return rowspan;
    }

    public void setRowspan(String rowspan) {
        this.rowspan = rowspan;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }
    public String getColspan() {
        return colspan;
    }

    public void setColspan(String colspan) {
        this.colspan = colspan;
    }
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}