





import java.util.List;
import java.util.ArrayList;

public class gaml_S_Equations extends Statement, EquationDefinition {






    private List<gaml_S_Assignment> gaml_s_assignments;


    public gaml_S_Equations(
    ) {
        super(
        );
        this.gaml_s_assignments = new ArrayList<>();
    }

    public gaml_S_Equations(
        ArrayList<gaml_S_Assignment> gaml_s_assignments    ) {
        this.gaml_s_assignments = gaml_s_assignments;
    }


    public List<gaml_S_Assignment> getGaml_s_assignments() {
        return gaml_s_assignments;
    }

    public void addGaml_s_assignment(Gaml_s_assignment gaml_s_assignment) {
        this.gaml_s_assignments.add(gaml_s_assignment);
    }

}