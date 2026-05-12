





import java.util.List;
import java.util.ArrayList;

public class HTML_TD extends TABLEElement {

    private String align;
    private String width;
    private String colspan;
    private String rowspan;
    private String valign;



    public HTML_TD(
        String align,        String width,        String colspan,        String rowspan,        String valign    ) {
        super(
        );
        this.align = align;
        this.width = width;
        this.colspan = colspan;
        this.rowspan = rowspan;
        this.valign = valign;
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
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }


}