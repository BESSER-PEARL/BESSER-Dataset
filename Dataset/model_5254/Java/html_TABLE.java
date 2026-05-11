





import java.util.List;
import java.util.ArrayList;

public class html_TABLE extends TABLEElement {

    private String width;
    private String border;
    private String cellspacing;
    private String cellpadding;



    public html_TABLE(
        String width,        String border,        String cellspacing,        String cellpadding    ) {
        super(
        );
        this.width = width;
        this.border = border;
        this.cellspacing = cellspacing;
        this.cellpadding = cellpadding;
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