





import java.util.List;
import java.util.ArrayList;

public class edu_Program extends ASTNode {






    private List<edu_FunctionDeclaration> edu_functiondeclarations;


    public edu_Program(
    ) {
        super(
        );
        this.edu_functiondeclarations = new ArrayList<>();
    }

    public edu_Program(
        ArrayList<edu_FunctionDeclaration> edu_functiondeclarations    ) {
        this.edu_functiondeclarations = edu_functiondeclarations;
    }


    public List<edu_FunctionDeclaration> getEdu_functiondeclarations() {
        return edu_functiondeclarations;
    }

    public void addEdu_functiondeclaration(Edu_functiondeclaration edu_functiondeclaration) {
        this.edu_functiondeclarations.add(edu_functiondeclaration);
    }

}