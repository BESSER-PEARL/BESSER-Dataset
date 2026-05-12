





import java.util.List;
import java.util.ArrayList;

public class HTML_TR extends TABLEElement {

    private String valign;
    private String align;





    private List<TD> tds;


    public HTML_TR(
        String valign,        String align    ) {
        super(
        );
        this.valign = valign;
        this.align = align;
        this.tds = new ArrayList<>();
    }

    public HTML_TR(
        String valign,        String align        ArrayList<TD> tds    ) {
        this.valign = valign;
        this.align = align;
        this.tds = tds;
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

    public List<TD> getTds() {
        return tds;
    }

    public void addTd(Td td) {
        this.tds.add(td);
    }

}