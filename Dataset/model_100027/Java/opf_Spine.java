





import java.util.List;
import java.util.ArrayList;

public class opf_Spine  {

    private String toc;





    private List<opf_Itemref> opf_itemrefs;




    private opf_Package opf_package;


    public opf_Spine(
        String toc    ) {
        this.toc = toc;
        this.opf_itemrefs = new ArrayList<>();
    }

    public opf_Spine(
        String toc        ArrayList<opf_Itemref> opf_itemrefs    ) {
        this.toc = toc;
        this.opf_itemrefs = opf_itemrefs;
    }

    public String getToc() {
        return toc;
    }

    public void setToc(String toc) {
        this.toc = toc;
    }

    public List<opf_Itemref> getOpf_itemrefs() {
        return opf_itemrefs;
    }

    public void addOpf_itemref(Opf_itemref opf_itemref) {
        this.opf_itemrefs.add(opf_itemref);
    }
    public opf_Package getOpf_package() {
        return opf_package;
    }

    public void setOpf_package(opf_Package opf_package) {
        this.opf_package = opf_package;
    }

}