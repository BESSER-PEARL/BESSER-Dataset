





import java.util.List;
import java.util.ArrayList;

public class spem_Milestone extends WorkBreakdownElement {






    private List<spem_WorkProductUse> spem_workproductuses;


    public spem_Milestone(
    ) {
        super(
        );
        this.spem_workproductuses = new ArrayList<>();
    }

    public spem_Milestone(
        ArrayList<spem_WorkProductUse> spem_workproductuses    ) {
        this.spem_workproductuses = spem_workproductuses;
    }


    public List<spem_WorkProductUse> getSpem_workproductuses() {
        return spem_workproductuses;
    }

    public void addSpem_workproductuse(Spem_workproductuse spem_workproductuse) {
        this.spem_workproductuses.add(spem_workproductuse);
    }

}