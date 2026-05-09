





import java.util.List;
import java.util.ArrayList;

public class javaDsl_Block extends Statement {






    private javaDsl_MethodDeclaration javadsl_methoddeclaration;




    private javaDsl_StaticInitializer javadsl_staticinitializer;


    public javaDsl_Block(
    ) {
        super(
        );
    }



    public javaDsl_MethodDeclaration getJavadsl_methoddeclaration() {
        return javadsl_methoddeclaration;
    }

    public void setJavadsl_methoddeclaration(javaDsl_MethodDeclaration javadsl_methoddeclaration) {
        this.javadsl_methoddeclaration = javadsl_methoddeclaration;
    }
    public javaDsl_StaticInitializer getJavadsl_staticinitializer() {
        return javadsl_staticinitializer;
    }

    public void setJavadsl_staticinitializer(javaDsl_StaticInitializer javadsl_staticinitializer) {
        this.javadsl_staticinitializer = javadsl_staticinitializer;
    }

}