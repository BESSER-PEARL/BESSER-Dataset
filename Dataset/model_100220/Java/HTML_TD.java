





import java.util.List;
import java.util.ArrayList;

public class HTML_TD extends TABLEElement {

    private String align;
    private String rowspan;
    private String valign;
    private String colspan;
    private String width;



    public HTML_TD(
        String align,        String rowspan,        String valign,        String colspan,        String width    ) {
        super(
        );
        this.align = align;
        this.rowspan = rowspan;
        this.valign = valign;
        this.colspan = colspan;
        this.width = width;
    }


    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
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


}