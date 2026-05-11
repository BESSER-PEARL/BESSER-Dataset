





import java.util.List;
import java.util.ArrayList;

public class html_TABLE extends TABLEElement {

    private String border;
    private String cellspacing;
    private String cellpadding;
    private String width;





    private List<html_TR> html_trs;




    private html_TR html_tr;


    public html_TABLE(
        String border,        String cellspacing,        String cellpadding,        String width    ) {
        super(
        );
        this.border = border;
        this.cellspacing = cellspacing;
        this.cellpadding = cellpadding;
        this.width = width;
        this.html_trs = new ArrayList<>();
    }

    public html_TABLE(
        String border,        String cellspacing,        String cellpadding,        String width        ArrayList<html_TR> html_trs    ) {
        this.border = border;
        this.cellspacing = cellspacing;
        this.cellpadding = cellpadding;
        this.width = width;
        this.html_trs = html_trs;
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
    public String getCellpadding() {
        return cellpadding;
    }

    public void setCellpadding(String cellpadding) {
        this.cellpadding = cellpadding;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }

    public List<html_TR> getHtml_trs() {
        return html_trs;
    }

    public void addHtml_tr(Html_tr html_tr) {
        this.html_trs.add(html_tr);
    }
    public html_TR getHtml_tr() {
        return html_tr;
    }

    public void setHtml_tr(html_TR html_tr) {
        this.html_tr = html_tr;
    }

}