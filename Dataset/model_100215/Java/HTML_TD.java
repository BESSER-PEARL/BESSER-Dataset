





import java.util.List;
import java.util.ArrayList;

public class HTML_TD extends TABLEElement {

    private String colspan;
    private String valign;
    private String rowspan;
    private String width;
    private String align;





    private TR tr;


    public HTML_TD(
        String colspan,        String valign,        String rowspan,        String width,        String align    ) {
        super(
        );
        this.colspan = colspan;
        this.valign = valign;
        this.rowspan = rowspan;
        this.width = width;
        this.align = align;
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
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }

    public TR getTr() {
        return tr;
    }

    public void setTr(TR tr) {
        this.tr = tr;
    }

}