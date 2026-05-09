





import java.util.List;
import java.util.ArrayList;

public class umm_Assembled extends AssembledBase {






    private List<umm_Subset> umm_subsets;




    private List<umm_Original> umm_originals;


    public umm_Assembled(
    ) {
        super(
        );
        this.umm_subsets = new ArrayList<>();
        this.umm_originals = new ArrayList<>();
    }

    public umm_Assembled(
        ArrayList<umm_Subset> umm_subsets,        ArrayList<umm_Original> umm_originals    ) {
        this.umm_subsets = umm_subsets;
        this.umm_originals = umm_originals;
    }


    public List<umm_Subset> getUmm_subsets() {
        return umm_subsets;
    }

    public void addUmm_subset(Umm_subset umm_subset) {
        this.umm_subsets.add(umm_subset);
    }
    public List<umm_Original> getUmm_originals() {
        return umm_originals;
    }

    public void addUmm_original(Umm_original umm_original) {
        this.umm_originals.add(umm_original);
    }

}