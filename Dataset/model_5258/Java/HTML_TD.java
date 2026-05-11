





import java.util.List;
import java.util.ArrayList;

public class HTML_TD extends TABLEElement {

    private String rowspan;
    private String align;
    private String colspan;
    private String width;
    private String valign;



    public HTML_TD(
        String rowspan,        String align,        String colspan,        String width,        String valign    ) {
        super(
        );
        this.rowspan = rowspan;
        this.align = align;
        this.colspan = colspan;
        this.width = width;
        this.valign = valign;
    }


    public String getRowspan() {
        return rowspan;
    }

    public void setRowspan(String rowspan) {
        this.rowspan = rowspan;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getColspan() {
        return colspan;
    }

    public void setColspan(String colspan) {
        this.colspan = colspan;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }


}