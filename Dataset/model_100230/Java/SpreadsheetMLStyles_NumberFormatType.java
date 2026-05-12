





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_NumberFormatType  {

    private String format;





    private StyleType styletype;


    public SpreadsheetMLStyles_NumberFormatType(
        String format    ) {
        this.format = format;
    }


    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }

    public StyleType getStyletype() {
        return styletype;
    }

    public void setStyletype(StyleType styletype) {
        this.styletype = styletype;
    }

}