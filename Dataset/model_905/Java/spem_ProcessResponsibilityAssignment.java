





import java.util.List;
import java.util.ArrayList;

public class spem_ProcessResponsibilityAssignment extends BreakdownElement {






    private spem_WorkProductUse spem_workproductuse;




    private List<spem_RoleUse> spem_roleuses;


    public spem_ProcessResponsibilityAssignment(
    ) {
        super(
        );
        this.spem_roleuses = new ArrayList<>();
    }

    public spem_ProcessResponsibilityAssignment(
        ArrayList<spem_RoleUse> spem_roleuses    ) {
        this.spem_roleuses = spem_roleuses;
    }


    public spem_WorkProductUse getSpem_workproductuse() {
        return spem_workproductuse;
    }

    public void setSpem_workproductuse(spem_WorkProductUse spem_workproductuse) {
        this.spem_workproductuse = spem_workproductuse;
    }
    public List<spem_RoleUse> getSpem_roleuses() {
        return spem_roleuses;
    }

    public void addSpem_roleuse(Spem_roleuse spem_roleuse) {
        this.spem_roleuses.add(spem_roleuse);
    }

}