





import java.util.List;
import java.util.ArrayList;

public class html_TD extends TABLEElement {

    private String colspan;
    private String rowspan;
    private String valign;
    private String width;
    private String align;





    private html_TR html_tr;




    private html_TR html_tr;


    public html_TD(
        String colspan,        String rowspan,        String valign,        String width,        String align    ) {
        super(
        );
        this.colspan = colspan;
        this.rowspan = rowspan;
        this.valign = valign;
        this.width = width;
        this.align = align;
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