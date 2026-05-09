





import java.util.List;
import java.util.ArrayList;

public class javaMM_EnumConstantDeclaration extends VariableDeclaration, BodyDeclaration {






    private javaMM_AnonymousClassDeclaration javamm_anonymousclassdeclaration;




    private List<javaMM_Expression> javamm_expressions;


    public javaMM_EnumConstantDeclaration(
    ) {
        super(
        );
        this.javamm_expressions = new ArrayList<>();
    }

    public javaMM_EnumConstantDeclaration(
        ArrayList<javaMM_Expression> javamm_expressions    ) {
        this.javamm_expressions = javamm_expressions;
    }


    public javaMM_AnonymousClassDeclaration getJavamm_anonymousclassdeclaration() {
        return javamm_anonymousclassdeclaration;
    }

    public void setJavamm_anonymousclassdeclaration(javaMM_AnonymousClassDeclaration javamm_anonymousclassdeclaration) {
        this.javamm_anonymousclassdeclaration = javamm_anonymousclassdeclaration;
    }
    public List<javaMM_Expression> getJavamm_expressions() {
        return javamm_expressions;
    }

    public void addJavamm_expression(Javamm_expression javamm_expression) {
        this.javamm_expressions.add(javamm_expression);
    }

}