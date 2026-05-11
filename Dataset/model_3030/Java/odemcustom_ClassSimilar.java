





import java.util.List;
import java.util.ArrayList;

public class odemcustom_ClassSimilar extends EmbeddableExtensionsContainer, ModifierExtensionsContainer {






    private List<odemcustom_Procedure> odemcustom_procedures;


    public odemcustom_ClassSimilar(
    ) {
        super(
        );
        this.odemcustom_procedures = new ArrayList<>();
    }

    public odemcustom_ClassSimilar(
        ArrayList<odemcustom_Procedure> odemcustom_procedures    ) {
        this.odemcustom_procedures = odemcustom_procedures;
    }


    public List<odemcustom_Procedure> getOdemcustom_procedures() {
        return odemcustom_procedures;
    }

    public void addOdemcustom_procedure(Odemcustom_procedure odemcustom_procedure) {
        this.odemcustom_procedures.add(odemcustom_procedure);
    }

}