





import java.util.List;
import java.util.ArrayList;

public class HTML_TD extends TABLEElement {

    private String rowspan;
    private String colspan;
    private String align;
    private String valign;
    private String width;



    public HTML_TD(
        String rowspan,        String colspan,        String align,        String valign,        String width    ) {
        super(
        );
        this.rowspan = rowspan;
        this.colspan = colspan;
        this.align = align;
        this.valign = valign;
        this.width = width;
    }


    public String getRowspan() {
        return rowspan;
    }

    public void setRowspan(String rowspan) {
        this.rowspan = rowspan;
    }
    public String getColspan() {
        return colspan;
    }

    public void setColspan(String colspan) {
        this.colspan = colspan;
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
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}