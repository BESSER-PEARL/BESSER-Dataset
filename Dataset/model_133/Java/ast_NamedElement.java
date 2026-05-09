





import java.util.List;
import java.util.ArrayList;

public class ast_NamedElement extends EJBase {






    private ast_Identifier ast_identifier;


    public ast_NamedElement(
    ) {
        super(
        );
    }



    public ast_Identifier getAst_identifier() {
        return ast_identifier;
    }

    public void setAst_identifier(ast_Identifier ast_identifier) {
        this.ast_identifier = ast_identifier;
    }

}