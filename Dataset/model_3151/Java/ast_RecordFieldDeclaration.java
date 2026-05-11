





import java.util.List;
import java.util.ArrayList;

public class ast_RecordFieldDeclaration  {

    private String name;





    private ast_RecordDefinition ast_recorddefinition;


    public ast_RecordFieldDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ast_RecordDefinition getAst_recorddefinition() {
        return ast_recorddefinition;
    }

    public void setAst_recorddefinition(ast_RecordDefinition ast_recorddefinition) {
        this.ast_recorddefinition = ast_recorddefinition;
    }

}