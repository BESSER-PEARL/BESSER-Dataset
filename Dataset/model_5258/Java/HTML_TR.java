





import java.util.List;
import java.util.ArrayList;

public class HTML_TR extends TABLEElement {

    private String valign;
    private String align;



    public HTML_TR(
        String valign,        String align    ) {
        super(
        );
        this.valign = valign;
        this.align = align;
    }


    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }


}