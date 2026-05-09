





import java.util.List;
import java.util.ArrayList;

public class javaDsl_AbstractMethodDeclaration extends InterfaceMemberDeclaration {






    private javaDsl_ResultType javadsl_resulttype;




    private javaDsl_Exceptions javadsl_exceptions;




    private javaDsl_MethodDeclarator javadsl_methoddeclarator;


    public javaDsl_AbstractMethodDeclaration(
    ) {
        super(
        );
    }



    public javaDsl_ResultType getJavadsl_resulttype() {
        return javadsl_resulttype;
    }

    public void setJavadsl_resulttype(javaDsl_ResultType javadsl_resulttype) {
        this.javadsl_resulttype = javadsl_resulttype;
    }
    public javaDsl_Exceptions getJavadsl_exceptions() {
        return javadsl_exceptions;
    }

    public void setJavadsl_exceptions(javaDsl_Exceptions javadsl_exceptions) {
        this.javadsl_exceptions = javadsl_exceptions;
    }
    public javaDsl_MethodDeclarator getJavadsl_methoddeclarator() {
        return javadsl_methoddeclarator;
    }

    public void setJavadsl_methoddeclarator(javaDsl_MethodDeclarator javadsl_methoddeclarator) {
        this.javadsl_methoddeclarator = javadsl_methoddeclarator;
    }

}