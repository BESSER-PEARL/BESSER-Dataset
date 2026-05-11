





import java.util.List;
import java.util.ArrayList;

public class refinher2_DG  {






    private List<refinher2_BB> refinher2_bbs;


    public refinher2_DG(
    ) {
        this.refinher2_bbs = new ArrayList<>();
    }

    public refinher2_DG(
        ArrayList<refinher2_BB> refinher2_bbs    ) {
        this.refinher2_bbs = refinher2_bbs;
    }


    public List<refinher2_BB> getRefinher2_bbs() {
        return refinher2_bbs;
    }

    public void addRefinher2_bb(Refinher2_bb refinher2_bb) {
        this.refinher2_bbs.add(refinher2_bb);
    }

}