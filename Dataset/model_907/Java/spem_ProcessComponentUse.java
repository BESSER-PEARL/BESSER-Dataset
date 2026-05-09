





import java.util.List;
import java.util.ArrayList;

public class spem_ProcessComponentUse extends MethodContentUse {






    private List<spem_WorkProductPort> spem_workproductports;


    public spem_ProcessComponentUse(
    ) {
        super(
        );
        this.spem_workproductports = new ArrayList<>();
    }

    public spem_ProcessComponentUse(
        ArrayList<spem_WorkProductPort> spem_workproductports    ) {
        this.spem_workproductports = spem_workproductports;
    }


    public List<spem_WorkProductPort> getSpem_workproductports() {
        return spem_workproductports;
    }

    public void addSpem_workproductport(Spem_workproductport spem_workproductport) {
        this.spem_workproductports.add(spem_workproductport);
    }

}