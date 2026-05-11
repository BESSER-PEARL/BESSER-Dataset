





import java.util.List;
import java.util.ArrayList;

public class HTML_TD extends TABLEElement {

    private String rowspan;
    private String valign;
    private String align;
    private String colspan;
    private String width;





    private HTML_TR html_tr;




    private HTML_TR html_tr;


    public HTML_TD(
        String rowspan,        String valign,        String align,        String colspan,        String width    ) {
        super(
        );
        this.rowspan = rowspan;
        this.valign = valign;
        this.align = align;
        this.colspan = colspan;
        this.width = width;
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

    public HTML_TR getHtml_tr() {
        return html_tr;
    }

    public void setHtml_tr(HTML_TR html_tr) {
        this.html_tr = html_tr;
    }
    public HTML_TR getHtml_tr() {
        return html_tr;
    }

    public void setHtml_tr(HTML_TR html_tr) {
        this.html_tr = html_tr;
    }

}