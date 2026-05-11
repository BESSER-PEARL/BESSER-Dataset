





import java.util.List;
import java.util.ArrayList;

public class ast_TypeAliasDefinition extends DataTypeDefinition {






    private ast_PrimitiveType ast_primitivetype;


    public ast_TypeAliasDefinition(
    ) {
        super(
        );
    }



    public ast_PrimitiveType getAst_primitivetype() {
        return ast_primitivetype;
    }

    public void setAst_primitivetype(ast_PrimitiveType ast_primitivetype) {
        this.ast_primitivetype = ast_primitivetype;
    }

}