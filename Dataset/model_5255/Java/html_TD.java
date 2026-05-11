





import java.util.List;
import java.util.ArrayList;

public class html_TD extends TABLEElement {

    private String align;
    private String valign;
    private String width;
    private String rowspan;
    private String colspan;





    private html_TR html_tr;




    private html_TR html_tr;


    public html_TD(
        String align,        String valign,        String width,        String rowspan,        String colspan    ) {
        super(
        );
        this.align = align;
        this.valign = valign;
        this.width = width;
        this.rowspan = rowspan;
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

    public html_TR getHtml_tr() {
        return html_tr;
    }

    public void setHtml_tr(html_TR html_tr) {
        this.html_tr = html_tr;
    }
    public html_TR getHtml_tr() {
        return html_tr;
    }

    public void setHtml_tr(html_TR html_tr) {
        this.html_tr = html_tr;
    }

}