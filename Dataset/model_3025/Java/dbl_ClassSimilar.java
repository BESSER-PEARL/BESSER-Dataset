





import java.util.List;
import java.util.ArrayList;

public class dbl_ClassSimilar extends ModifierExtensionsContainer, EmbeddableExtensionsContainer {






    private List<dbl_Variable> dbl_variables;




    private List<dbl_Procedure> dbl_procedures;


    public dbl_ClassSimilar(
    ) {
        super(
        );
        this.dbl_variables = new ArrayList<>();
        this.dbl_procedures = new ArrayList<>();
    }

    public dbl_ClassSimilar(
        ArrayList<dbl_Variable> dbl_variables,        ArrayList<dbl_Procedure> dbl_procedures    ) {
        this.dbl_variables = dbl_variables;
        this.dbl_procedures = dbl_procedures;
    }


    public List<dbl_Variable> getDbl_variables() {
        return dbl_variables;
    }

    public void addDbl_variable(Dbl_variable dbl_variable) {
        this.dbl_variables.add(dbl_variable);
    }
    public List<dbl_Procedure> getDbl_procedures() {
        return dbl_procedures;
    }

    public void addDbl_procedure(Dbl_procedure dbl_procedure) {
        this.dbl_procedures.add(dbl_procedure);
    }

}