





import java.util.List;
import java.util.ArrayList;

public class defaultname_TABLE extends TABLEElement {

    private String border;
    private String cellpadding;
    private String cellspacing;
    private String width;





    private List<defaultname_TR> defaultname_trs;




    private defaultname_TR defaultname_tr;


    public defaultname_TABLE(
        String border,        String cellpadding,        String cellspacing,        String width    ) {
        super(
        );
        this.border = border;
        this.cellpadding = cellpadding;
        this.cellspacing = cellspacing;
        this.width = width;
        this.defaultname_trs = new ArrayList<>();
    }

    public defaultname_TABLE(
        String border,        String cellpadding,        String cellspacing,        String width        ArrayList<defaultname_TR> defaultname_trs    ) {
        this.border = border;
        this.cellpadding = cellpadding;
        this.cellspacing = cellspacing;
        this.width = width;
        this.defaultname_trs = defaultname_trs;
    }

    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getCellpadding() {
        return cellpadding;
    }

    public void setCellpadding(String cellpadding) {
        this.cellpadding = cellpadding;
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

    public List<defaultname_TR> getDefaultname_trs() {
        return defaultname_trs;
    }

    public void addDefaultname_tr(Defaultname_tr defaultname_tr) {
        this.defaultname_trs.add(defaultname_tr);
    }
    public defaultname_TR getDefaultname_tr() {
        return defaultname_tr;
    }

    public void setDefaultname_tr(defaultname_TR defaultname_tr) {
        this.defaultname_tr = defaultname_tr;
    }

}