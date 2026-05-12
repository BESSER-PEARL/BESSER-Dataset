





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_HeaderOrFooterElt  {

    private String data;
    private String margin;



    public SpreadsheetMLStyles_HeaderOrFooterElt(
        String data,        String margin    ) {
        this.data = data;
        this.margin = margin;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getMargin() {
        return margin;
    }

    public void setMargin(String margin) {
        this.margin = margin;
    }


}