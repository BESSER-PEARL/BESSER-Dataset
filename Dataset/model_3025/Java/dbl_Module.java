





import java.util.List;
import java.util.ArrayList;

public class dbl_Module extends Construct, EmbeddableExtensionsContainer, NamedElement {






    private List<dbl_Procedure> dbl_procedures;


    public dbl_Module(
    ) {
        super(
        );
        this.dbl_procedures = new ArrayList<>();
    }

    public dbl_Module(
        ArrayList<dbl_Procedure> dbl_procedures    ) {
        this.dbl_procedures = dbl_procedures;
    }


    public List<dbl_Procedure> getDbl_procedures() {
        return dbl_procedures;
    }

    public void addDbl_procedure(Dbl_procedure dbl_procedure) {
        this.dbl_procedures.add(dbl_procedure);
    }

}