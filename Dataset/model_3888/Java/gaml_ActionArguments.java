





import java.util.List;
import java.util.ArrayList;

public class gaml_ActionArguments  {






    private gaml_S_Definition gaml_s_definition;




    private List<gaml_ArgumentDefinition> gaml_argumentdefinitions;


    public gaml_ActionArguments(
    ) {
        this.gaml_argumentdefinitions = new ArrayList<>();
    }

    public gaml_ActionArguments(
        ArrayList<gaml_ArgumentDefinition> gaml_argumentdefinitions    ) {
        this.gaml_argumentdefinitions = gaml_argumentdefinitions;
    }


    public gaml_S_Definition getGaml_s_definition() {
        return gaml_s_definition;
    }

    public void setGaml_s_definition(gaml_S_Definition gaml_s_definition) {
        this.gaml_s_definition = gaml_s_definition;
    }
    public List<gaml_ArgumentDefinition> getGaml_argumentdefinitions() {
        return gaml_argumentdefinitions;
    }

    public void addGaml_argumentdefinition(Gaml_argumentdefinition gaml_argumentdefinition) {
        this.gaml_argumentdefinitions.add(gaml_argumentdefinition);
    }

}