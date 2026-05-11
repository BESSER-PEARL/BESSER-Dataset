





import java.util.List;
import java.util.ArrayList;

public class html_TD extends TABLEElement {

    private String width;
    private String valign;
    private String colspan;
    private String align;
    private String rowspan;



    public html_TD(
        String width,        String valign,        String colspan,        String align,        String rowspan    ) {
        super(
        );
        this.width = width;
        this.valign = valign;
        this.colspan = colspan;
        this.align = align;
        this.rowspan = rowspan;
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
    public String getRowspan() {
        return rowspan;
    }

    public void setRowspan(String rowspan) {
        this.rowspan = rowspan;
    }


}