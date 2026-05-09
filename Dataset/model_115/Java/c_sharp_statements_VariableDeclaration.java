





import java.util.List;
import java.util.ArrayList;

public class c_sharp_statements_VariableDeclaration extends statements_ResourceAcquisition, statements_ForInitializer {






    private VariableDeclarator variabledeclarator;




    private Type type;


    public c_sharp_statements_VariableDeclaration(
    ) {
        super(
        );
    }



    public VariableDeclarator getVariabledeclarator() {
        return variabledeclarator;
    }

    public void setVariabledeclarator(VariableDeclarator variabledeclarator) {
        this.variabledeclarator = variabledeclarator;
    }
    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}