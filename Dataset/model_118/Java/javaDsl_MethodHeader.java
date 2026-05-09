





import java.util.List;
import java.util.ArrayList;

public class javaDsl_MethodHeader  {

    private String modifiers;





    private javaDsl_Exceptions javadsl_exceptions;




    private javaDsl_MethodDeclaration javadsl_methoddeclaration;


    public javaDsl_MethodHeader(
        String modifiers    ) {
        this.modifiers = modifiers;
    }


    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }

    public javaDsl_Exceptions getJavadsl_exceptions() {
        return javadsl_exceptions;
    }

    public void setJavadsl_exceptions(javaDsl_Exceptions javadsl_exceptions) {
        this.javadsl_exceptions = javadsl_exceptions;
    }
    public javaDsl_MethodDeclaration getJavadsl_methoddeclaration() {
        return javadsl_methoddeclaration;
    }

    public void setJavadsl_methoddeclaration(javaDsl_MethodDeclaration javadsl_methoddeclaration) {
        this.javadsl_methoddeclaration = javadsl_methoddeclaration;
    }

}