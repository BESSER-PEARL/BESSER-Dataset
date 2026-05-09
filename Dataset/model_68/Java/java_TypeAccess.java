





import java.util.List;
import java.util.ArrayList;

public class java_TypeAccess extends Expression, NamespaceAccess {






    private java_SingleVariableDeclaration java_singlevariabledeclaration;




    private java_WildCardType java_wildcardtype;




    private java_TypeLiteral java_typeliteral;


    public java_TypeAccess(
    ) {
        super(
        );
    }



    public java_SingleVariableDeclaration getJava_singlevariabledeclaration() {
        return java_singlevariabledeclaration;
    }

    public void setJava_singlevariabledeclaration(java_SingleVariableDeclaration java_singlevariabledeclaration) {
        this.java_singlevariabledeclaration = java_singlevariabledeclaration;
    }
    public java_WildCardType getJava_wildcardtype() {
        return java_wildcardtype;
    }

    public void setJava_wildcardtype(java_WildCardType java_wildcardtype) {
        this.java_wildcardtype = java_wildcardtype;
    }
    public java_TypeLiteral getJava_typeliteral() {
        return java_typeliteral;
    }

    public void setJava_typeliteral(java_TypeLiteral java_typeliteral) {
        this.java_typeliteral = java_typeliteral;
    }

}