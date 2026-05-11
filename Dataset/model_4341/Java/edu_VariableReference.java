





import java.util.List;
import java.util.ArrayList;

public class edu_VariableReference extends SymbolReference {






    private edu_Assignment edu_assignment;




    private edu_VariableDeclaration edu_variabledeclaration;


    public edu_VariableReference(
    ) {
        super(
        );
    }



    public edu_Assignment getEdu_assignment() {
        return edu_assignment;
    }

    public void setEdu_assignment(edu_Assignment edu_assignment) {
        this.edu_assignment = edu_assignment;
    }
    public edu_VariableDeclaration getEdu_variabledeclaration() {
        return edu_variabledeclaration;
    }

    public void setEdu_variabledeclaration(edu_VariableDeclaration edu_variabledeclaration) {
        this.edu_variabledeclaration = edu_variabledeclaration;
    }

}