





import java.util.List;
import java.util.ArrayList;

public class HTML_TD extends TABLEElement {

    private String align;
    private String width;
    private String valign;
    private String colspan;
    private String rowspan;





    private HTML_TR html_tr;




    private HTML_TR html_tr;


    public HTML_TD(
        String align,        String width,        String valign,        String colspan,        String rowspan    ) {
        super(
        );
        this.align = align;
        this.width = width;
        this.valign = valign;
        this.colspan = colspan;
        this.rowspan = rowspan;
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
    public String getRowspan() {
        return rowspan;
    }

    public void setRowspan(String rowspan) {
        this.rowspan = rowspan;
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