





import java.util.List;
import java.util.ArrayList;

public class html_TD extends TABLEElement {

    private String valign;
    private String rowspan;
    private String width;
    private String colspan;
    private String align;



    public html_TD(
        String valign,        String rowspan,        String width,        String colspan,        String align    ) {
        super(
        );
        this.valign = valign;
        this.rowspan = rowspan;
        this.width = width;
        this.colspan = colspan;
        this.align = align;
    }


    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
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


}