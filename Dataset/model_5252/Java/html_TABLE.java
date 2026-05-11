





import java.util.List;
import java.util.ArrayList;

public class html_TABLE extends TABLEElement {

    private String cellpadding;
    private String border;
    private String width;
    private String cellspacing;



    public html_TABLE(
        String cellpadding,        String border,        String width,        String cellspacing    ) {
        super(
        );
        this.cellpadding = cellpadding;
        this.border = border;
        this.width = width;
        this.cellspacing = cellspacing;
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


}