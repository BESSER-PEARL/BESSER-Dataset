





import java.util.List;
import java.util.ArrayList;

public class OCL_OclModule extends Package {






    private List<OclModuleElement> oclmoduleelements;


    public OCL_OclModule(
    ) {
        super(
        );
        this.oclmoduleelements = new ArrayList<>();
    }

    public OCL_OclModule(
        ArrayList<OclModuleElement> oclmoduleelements    ) {
        this.oclmoduleelements = oclmoduleelements;
    }


    public List<OclModuleElement> getOclmoduleelements() {
        return oclmoduleelements;
    }

    public void addOclmoduleelement(Oclmoduleelement oclmoduleelement) {
        this.oclmoduleelements.add(oclmoduleelement);
    }

}