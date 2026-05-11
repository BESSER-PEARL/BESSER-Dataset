





import java.util.List;
import java.util.ArrayList;

public class xhtml_Block  {

    private String mixed;
    private String block;





    private List<xhtml_P> xhtml_ps;




    private List<xhtml_Div> xhtml_divs;


    public xhtml_Block(
        String mixed,        String block    ) {
        this.mixed = mixed;
        this.block = block;
        this.xhtml_ps = new ArrayList<>();
        this.xhtml_divs = new ArrayList<>();
    }

    public xhtml_Block(
        String mixed,        String block        ArrayList<xhtml_P> xhtml_ps,        ArrayList<xhtml_Div> xhtml_divs    ) {
        this.mixed = mixed;
        this.block = block;
        this.xhtml_ps = xhtml_ps;
        this.xhtml_divs = xhtml_divs;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getBlock() {
        return block;
    }

    public void setBlock(String block) {
        this.block = block;
    }

    public List<xhtml_P> getXhtml_ps() {
        return xhtml_ps;
    }

    public void addXhtml_p(Xhtml_p xhtml_p) {
        this.xhtml_ps.add(xhtml_p);
    }
    public List<xhtml_Div> getXhtml_divs() {
        return xhtml_divs;
    }

    public void addXhtml_div(Xhtml_div xhtml_div) {
        this.xhtml_divs.add(xhtml_div);
    }

}