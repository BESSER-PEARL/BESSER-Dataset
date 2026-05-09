





import java.util.List;
import java.util.ArrayList;

public class OCL_OclType extends OclExpression {

    private String name;





    private VariableDeclaration variabledeclaration;


    public OCL_OclType(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public VariableDeclaration getVariabledeclaration() {
        return variabledeclaration;
    }

    public void setVariabledeclaration(VariableDeclaration variabledeclaration) {
        this.variabledeclaration = variabledeclaration;
    }

}