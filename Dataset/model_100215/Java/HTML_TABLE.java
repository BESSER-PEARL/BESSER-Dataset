





import java.util.List;
import java.util.ArrayList;

public class HTML_TABLE extends TABLEElement {

    private String cellspacing;
    private String width;
    private String cellpadding;
    private String border;





    private List<TR> trs;


    public HTML_TABLE(
        String cellspacing,        String width,        String cellpadding,        String border    ) {
        super(
        );
        this.cellspacing = cellspacing;
        this.width = width;
        this.cellpadding = cellpadding;
        this.border = border;
        this.trs = new ArrayList<>();
    }

    public HTML_TABLE(
        String cellspacing,        String width,        String cellpadding,        String border        ArrayList<TR> trs    ) {
        this.cellspacing = cellspacing;
        this.width = width;
        this.cellpadding = cellpadding;
        this.border = border;
        this.trs = trs;
    }

    public String getCellspacing() {
        return cellspacing;
    }

    public void setCellspacing(String cellspacing) {
        this.cellspacing = cellspacing;
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

    public List<TR> getTrs() {
        return trs;
    }

    public void addTr(Tr tr) {
        this.trs.add(tr);
    }

}