





import java.util.List;
import java.util.ArrayList;

public class ast_EnumerationLiteralDeclaration  {

    private String name;





    private ast_EnumerationDefinition ast_enumerationdefinition;


    public ast_EnumerationLiteralDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ast_EnumerationDefinition getAst_enumerationdefinition() {
        return ast_enumerationdefinition;
    }

    public void setAst_enumerationdefinition(ast_EnumerationDefinition ast_enumerationdefinition) {
        this.ast_enumerationdefinition = ast_enumerationdefinition;
    }

}