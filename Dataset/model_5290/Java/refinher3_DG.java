





import java.util.List;
import java.util.ArrayList;

public class refinher3_DG  {






    private List<refinher3_BB> refinher3_bbs;




    private List<refinher3_N> refinher3_ns;


    public refinher3_DG(
    ) {
        this.refinher3_bbs = new ArrayList<>();
        this.refinher3_ns = new ArrayList<>();
    }

    public refinher3_DG(
        ArrayList<refinher3_BB> refinher3_bbs,        ArrayList<refinher3_N> refinher3_ns    ) {
        this.refinher3_bbs = refinher3_bbs;
        this.refinher3_ns = refinher3_ns;
    }


    public List<refinher3_BB> getRefinher3_bbs() {
        return refinher3_bbs;
    }

    public void addRefinher3_bb(Refinher3_bb refinher3_bb) {
        this.refinher3_bbs.add(refinher3_bb);
    }
    public List<refinher3_N> getRefinher3_ns() {
        return refinher3_ns;
    }

    public void addRefinher3_n(Refinher3_n refinher3_n) {
        this.refinher3_ns.add(refinher3_n);
    }

}