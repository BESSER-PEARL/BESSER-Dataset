





import java.util.List;
import java.util.ArrayList;

public class atlext_OCL_OclExpression extends OCL_TypedElement, ATL_LocatedElement {

    private boolean implicitlyCasted;





    private PropertyCallExp propertycallexp;




    private LetExp letexp;




    private VariableDeclaration variabledeclaration;




    private IfExp ifexp;




    private IfExp ifexp;




    private IfExp ifexp;




    private CollectionExp collectionexp;


    public atlext_OCL_OclExpression(
        boolean implicitlyCasted    ) {
        super(
        );
        this.implicitlyCasted = implicitlyCasted;
    }


    public boolean getImplicitlycasted() {
        return implicitlyCasted;
    }

    public void setImplicitlycasted(boolean implicitlyCasted) {
        this.implicitlyCasted = implicitlyCasted;
    }

    public PropertyCallExp getPropertycallexp() {
        return propertycallexp;
    }

    public void setPropertycallexp(PropertyCallExp propertycallexp) {
        this.propertycallexp = propertycallexp;
    }
    public LetExp getLetexp() {
        return letexp;
    }

    public void setLetexp(LetExp letexp) {
        this.letexp = letexp;
    }
    public VariableDeclaration getVariabledeclaration() {
        return variabledeclaration;
    }

    public void setVariabledeclaration(VariableDeclaration variabledeclaration) {
        this.variabledeclaration = variabledeclaration;
    }
    public IfExp getIfexp() {
        return ifexp;
    }

    public void setIfexp(IfExp ifexp) {
        this.ifexp = ifexp;
    }
    public IfExp getIfexp() {
        return ifexp;
    }

    public void setIfexp(IfExp ifexp) {
        this.ifexp = ifexp;
    }
    public IfExp getIfexp() {
        return ifexp;
    }

    public void setIfexp(IfExp ifexp) {
        this.ifexp = ifexp;
    }
    public CollectionExp getCollectionexp() {
        return collectionexp;
    }

    public void setCollectionexp(CollectionExp collectionexp) {
        this.collectionexp = collectionexp;
    }

}