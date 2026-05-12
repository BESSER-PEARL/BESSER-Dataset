





import java.util.List;
import java.util.ArrayList;

public class HTML_TABLE extends TABLEElement {

    private String cellpadding;
    private String cellspacing;
    private String width;
    private String border;



    public HTML_TABLE(
        String cellpadding,        String cellspacing,        String width,        String border    ) {
        super(
        );
        this.cellpadding = cellpadding;
        this.cellspacing = cellspacing;
        this.width = width;
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
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }


}