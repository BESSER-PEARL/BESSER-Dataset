





import java.util.List;
import java.util.ArrayList;

public class HTML_TD extends HTMLElement {

    private String valign;
    private String colspan;
    private String height;
    private String width;
    private String align;
    private String rowspan;
    private String bgcolor;





    private HTML_TR html_tr;


    public HTML_TD(
        String valign,        String colspan,        String height,        String width,        String align,        String rowspan,        String bgcolor    ) {
        super(
        );
        this.valign = valign;
        this.colspan = colspan;
        this.height = height;
        this.width = width;
        this.align = align;
        this.rowspan = rowspan;
        this.bgcolor = bgcolor;
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
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
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
    public String getRowspan() {
        return rowspan;
    }

    public void setRowspan(String rowspan) {
        this.rowspan = rowspan;
    }
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }

    public HTML_TR getHtml_tr() {
        return html_tr;
    }

    public void setHtml_tr(HTML_TR html_tr) {
        this.html_tr = html_tr;
    }

}