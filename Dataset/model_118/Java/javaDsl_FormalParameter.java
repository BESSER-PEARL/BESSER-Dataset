





import java.util.List;
import java.util.ArrayList;

public class javaDsl_FormalParameter  {

    private String variable;





    private javaDsl_ConstructorDeclarator javadsl_constructordeclarator;


    public javaDsl_FormalParameter(
        String variable    ) {
        this.variable = variable;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }

    public javaDsl_ConstructorDeclarator getJavadsl_constructordeclarator() {
        return javadsl_constructordeclarator;
    }

    public void setJavadsl_constructordeclarator(javaDsl_ConstructorDeclarator javadsl_constructordeclarator) {
        this.javadsl_constructordeclarator = javadsl_constructordeclarator;
    }

}