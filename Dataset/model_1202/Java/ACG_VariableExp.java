





import java.util.List;
import java.util.ArrayList;

public class ACG_VariableExp extends Expression {






    private VariableDecl variabledecl;


    public ACG_VariableExp(
    ) {
        super(
        );
    }



    public VariableDecl getVariabledecl() {
        return variabledecl;
    }

    public void setVariabledecl(VariableDecl variabledecl) {
        this.variabledecl = variabledecl;
    }

}