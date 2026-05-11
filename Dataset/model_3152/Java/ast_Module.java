





import java.util.List;
import java.util.ArrayList;

public class ast_Module  {






    private List<ast_Definition> ast_definitions;


    public ast_Module(
    ) {
        this.ast_definitions = new ArrayList<>();
    }

    public ast_Module(
        ArrayList<ast_Definition> ast_definitions    ) {
        this.ast_definitions = ast_definitions;
    }


    public List<ast_Definition> getAst_definitions() {
        return ast_definitions;
    }

    public void addAst_definition(Ast_definition ast_definition) {
        this.ast_definitions.add(ast_definition);
    }

}