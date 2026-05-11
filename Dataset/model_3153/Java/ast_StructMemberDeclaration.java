





import java.util.List;
import java.util.ArrayList;

public class ast_StructMemberDeclaration  {

    private String name;





    private ast_StructDefinition ast_structdefinition;


    public ast_StructMemberDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ast_StructDefinition getAst_structdefinition() {
        return ast_structdefinition;
    }

    public void setAst_structdefinition(ast_StructDefinition ast_structdefinition) {
        this.ast_structdefinition = ast_structdefinition;
    }

}