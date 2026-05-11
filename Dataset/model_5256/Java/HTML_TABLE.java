





import java.util.List;
import java.util.ArrayList;

public class HTML_TABLE extends TABLEElement {

    private String width;
    private String cellpadding;
    private String border;
    private String cellspacing;





    private HTML_TR html_tr;




    private List<HTML_TR> html_trs;


    public HTML_TABLE(
        String width,        String cellpadding,        String border,        String cellspacing    ) {
        super(
        );
        this.width = width;
        this.cellpadding = cellpadding;
        this.border = border;
        this.cellspacing = cellspacing;
        this.html_trs = new ArrayList<>();
    }

    public HTML_TABLE(
        String width,        String cellpadding,        String border,        String cellspacing        ArrayList<HTML_TR> html_trs    ) {
        this.width = width;
        this.cellpadding = cellpadding;
        this.border = border;
        this.cellspacing = cellspacing;
        this.html_trs = html_trs;
    }

    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getCellpadding() {
        return cellpadding;
    }

    public void setCellpadding(String cellpadding) {
        this.cellpadding = cellpadding;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getCellspacing() {
        return cellspacing;
    }

    public void setCellspacing(String cellspacing) {
        this.cellspacing = cellspacing;
    }

    public HTML_TR getHtml_tr() {
        return html_tr;
    }

    public void setHtml_tr(HTML_TR html_tr) {
        this.html_tr = html_tr;
    }
    public List<HTML_TR> getHtml_trs() {
        return html_trs;
    }

    public void addHtml_tr(Html_tr html_tr) {
        this.html_trs.add(html_tr);
    }

}