





import java.util.List;
import java.util.ArrayList;

public class Html_TABLE extends TABLEElement {

    private String width;
    private String cellpadding;
    private String cellspacing;
    private String border;



    public Html_TABLE(
        String width,        String cellpadding,        String cellspacing,        String border    ) {
        super(
        );
        this.width = width;
        this.cellpadding = cellpadding;
        this.cellspacing = cellspacing;
        this.border = border;
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
    public String getCellspacing() {
        return cellspacing;
    }

    public void setCellspacing(String cellspacing) {
        this.cellspacing = cellspacing;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }


}