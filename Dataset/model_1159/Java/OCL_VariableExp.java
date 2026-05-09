





import java.util.List;
import java.util.ArrayList;

public class OCL_VariableExp extends OclExpression {






    private VariableDeclaration variabledeclaration;


    public OCL_VariableExp(
    ) {
        super(
        );
    }



    public VariableDeclaration getVariabledeclaration() {
        return variabledeclaration;
    }

    public void setVariabledeclaration(VariableDeclaration variabledeclaration) {
        this.variabledeclaration = variabledeclaration;
    }

}