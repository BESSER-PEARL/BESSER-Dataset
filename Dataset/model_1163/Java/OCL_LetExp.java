





import java.util.List;
import java.util.ArrayList;

public class OCL_LetExp extends OclExpression {






    private VariableDeclaration variabledeclaration;


    public OCL_LetExp(
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