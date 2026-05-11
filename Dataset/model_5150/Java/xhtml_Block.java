





import java.util.List;
import java.util.ArrayList;

public class xhtml_Block  {

    private String block;
    private String mixed;





    private List<xhtml_P> xhtml_ps;


    public xhtml_Block(
        String block,        String mixed    ) {
        this.block = block;
        this.mixed = mixed;
        this.xhtml_ps = new ArrayList<>();
    }

    public xhtml_Block(
        String block,        String mixed        ArrayList<xhtml_P> xhtml_ps    ) {
        this.block = block;
        this.mixed = mixed;
        this.xhtml_ps = xhtml_ps;
    }

    public String getBlock() {
        return block;
    }

    public void setBlock(String block) {
        this.block = block;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<xhtml_P> getXhtml_ps() {
        return xhtml_ps;
    }

    public void addXhtml_p(Xhtml_p xhtml_p) {
        this.xhtml_ps.add(xhtml_p);
    }

}