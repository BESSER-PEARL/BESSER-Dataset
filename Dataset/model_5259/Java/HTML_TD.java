





import java.util.List;
import java.util.ArrayList;

public class HTML_TD extends HTMLElement {

    private String align;
    private String valign;
    private String bgcolor;
    private String colspan;
    private String rowspan;
    private String width;
    private String height;



    public HTML_TD(
        String align,        String valign,        String bgcolor,        String colspan,        String rowspan,        String width,        String height    ) {
        super(
        );
        this.align = align;
        this.valign = valign;
        this.bgcolor = bgcolor;
        this.colspan = colspan;
        this.rowspan = rowspan;
        this.width = width;
        this.height = height;
    }


    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
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
    public String getRowspan() {
        return rowspan;
    }

    public void setRowspan(String rowspan) {
        this.rowspan = rowspan;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }


}