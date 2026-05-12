





import java.util.List;
import java.util.ArrayList;

public class HTML_TABLE extends TABLEElement {

    private String border;
    private String width;
    private String cellspacing;
    private String cellpadding;



    public HTML_TABLE(
        String border,        String width,        String cellspacing,        String cellpadding    ) {
        super(
        );
        this.border = border;
        this.width = width;
        this.cellspacing = cellspacing;
        this.cellpadding = cellpadding;
    }


    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
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


}