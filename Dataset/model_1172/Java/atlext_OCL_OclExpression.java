





import java.util.List;
import java.util.ArrayList;

public class atlext_OCL_OclExpression extends OCL_TypedElement, ATL_LocatedElement {

    private String implicitlyCasted;





    private VariableDeclaration variabledeclaration;




    private PropertyCallExp propertycallexp;


    public atlext_OCL_OclExpression(
        String implicitlyCasted    ) {
        super(
        );
        this.implicitlyCasted = implicitlyCasted;
    }


    public String getImplicitlycasted() {
        return implicitlyCasted;
    }

    public void setImplicitlycasted(String implicitlyCasted) {
        this.implicitlyCasted = implicitlyCasted;
    }

    public VariableDeclaration getVariabledeclaration() {
        return variabledeclaration;
    }

    public void setVariabledeclaration(VariableDeclaration variabledeclaration) {
        this.variabledeclaration = variabledeclaration;
    }
    public PropertyCallExp getPropertycallexp() {
        return propertycallexp;
    }

    public void setPropertycallexp(PropertyCallExp propertycallexp) {
        this.propertycallexp = propertycallexp;
    }

}