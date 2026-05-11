





import java.util.List;
import java.util.ArrayList;

public class Html_TR extends TABLEElement {

    private String align;
    private String valign;



    public Html_TR(
        String align,        String valign    ) {
        super(
        );
        this.align = align;
        this.valign = valign;
    }


    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }


}