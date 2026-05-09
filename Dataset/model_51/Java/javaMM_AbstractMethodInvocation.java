





import java.util.List;
import java.util.ArrayList;

public class javaMM_AbstractMethodInvocation extends ASTNode {






    private javaMM_AbstractMethodDeclaration javamm_abstractmethoddeclaration;




    private List<javaMM_Expression> javamm_expressions;




    private List<javaMM_TypeAccess> javamm_typeaccesss;




    private javaMM_AbstractMethodDeclaration javamm_abstractmethoddeclaration;


    public javaMM_AbstractMethodInvocation(
    ) {
        super(
        );
        this.javamm_expressions = new ArrayList<>();
        this.javamm_typeaccesss = new ArrayList<>();
    }

    public javaMM_AbstractMethodInvocation(
        ArrayList<javaMM_Expression> javamm_expressions,        ArrayList<javaMM_TypeAccess> javamm_typeaccesss    ) {
        this.javamm_expressions = javamm_expressions;
        this.javamm_typeaccesss = javamm_typeaccesss;
    }


    public javaMM_AbstractMethodDeclaration getJavamm_abstractmethoddeclaration() {
        return javamm_abstractmethoddeclaration;
    }

    public void setJavamm_abstractmethoddeclaration(javaMM_AbstractMethodDeclaration javamm_abstractmethoddeclaration) {
        this.javamm_abstractmethoddeclaration = javamm_abstractmethoddeclaration;
    }
    public List<javaMM_Expression> getJavamm_expressions() {
        return javamm_expressions;
    }

    public void addJavamm_expression(Javamm_expression javamm_expression) {
        this.javamm_expressions.add(javamm_expression);
    }
    public List<javaMM_TypeAccess> getJavamm_typeaccesss() {
        return javamm_typeaccesss;
    }

    public void addJavamm_typeaccess(Javamm_typeaccess javamm_typeaccess) {
        this.javamm_typeaccesss.add(javamm_typeaccess);
    }
    public javaMM_AbstractMethodDeclaration getJavamm_abstractmethoddeclaration() {
        return javamm_abstractmethoddeclaration;
    }

    public void setJavamm_abstractmethoddeclaration(javaMM_AbstractMethodDeclaration javamm_abstractmethoddeclaration) {
        this.javamm_abstractmethoddeclaration = javamm_abstractmethoddeclaration;
    }

}