





import java.util.List;
import java.util.ArrayList;

public class b_Definition  {

    private String name;





    private List<b_Variable> b_variables;




    private b_DefinitionCall b_definitioncall;




    private b_Definitions b_definitions;


    public b_Definition(
        String name    ) {
        this.name = name;
        this.b_variables = new ArrayList<>();
    }

    public b_Definition(
        String name        ArrayList<b_Variable> b_variables    ) {
        this.name = name;
        this.b_variables = b_variables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<b_Variable> getB_variables() {
        return b_variables;
    }

    public void addB_variable(B_variable b_variable) {
        this.b_variables.add(b_variable);
    }
    public b_DefinitionCall getB_definitioncall() {
        return b_definitioncall;
    }

    public void setB_definitioncall(b_DefinitionCall b_definitioncall) {
        this.b_definitioncall = b_definitioncall;
    }
    public b_Definitions getB_definitions() {
        return b_definitions;
    }

    public void setB_definitions(b_Definitions b_definitions) {
        this.b_definitions = b_definitions;
    }

}