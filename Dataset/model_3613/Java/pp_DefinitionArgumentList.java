





import java.util.List;
import java.util.ArrayList;

public class pp_DefinitionArgumentList  {






    private pp_Definition pp_definition;




    private pp_Lambda pp_lambda;




    private List<pp_DefinitionArgument> pp_definitionarguments;


    public pp_DefinitionArgumentList(
    ) {
        this.pp_definitionarguments = new ArrayList<>();
    }

    public pp_DefinitionArgumentList(
        ArrayList<pp_DefinitionArgument> pp_definitionarguments    ) {
        this.pp_definitionarguments = pp_definitionarguments;
    }


    public pp_Definition getPp_definition() {
        return pp_definition;
    }

    public void setPp_definition(pp_Definition pp_definition) {
        this.pp_definition = pp_definition;
    }
    public pp_Lambda getPp_lambda() {
        return pp_lambda;
    }

    public void setPp_lambda(pp_Lambda pp_lambda) {
        this.pp_lambda = pp_lambda;
    }
    public List<pp_DefinitionArgument> getPp_definitionarguments() {
        return pp_definitionarguments;
    }

    public void addPp_definitionargument(Pp_definitionargument pp_definitionargument) {
        this.pp_definitionarguments.add(pp_definitionargument);
    }

}