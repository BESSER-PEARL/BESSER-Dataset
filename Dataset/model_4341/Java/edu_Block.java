





import java.util.List;
import java.util.ArrayList;

public class edu_Block extends Statement {






    private edu_Program edu_program;




    private edu_FunctionDeclaration edu_functiondeclaration;




    private List<edu_Statement> edu_statements;


    public edu_Block(
    ) {
        super(
        );
        this.edu_statements = new ArrayList<>();
    }

    public edu_Block(
        ArrayList<edu_Statement> edu_statements    ) {
        this.edu_statements = edu_statements;
    }


    public edu_Program getEdu_program() {
        return edu_program;
    }

    public void setEdu_program(edu_Program edu_program) {
        this.edu_program = edu_program;
    }
    public edu_FunctionDeclaration getEdu_functiondeclaration() {
        return edu_functiondeclaration;
    }

    public void setEdu_functiondeclaration(edu_FunctionDeclaration edu_functiondeclaration) {
        this.edu_functiondeclaration = edu_functiondeclaration;
    }
    public List<edu_Statement> getEdu_statements() {
        return edu_statements;
    }

    public void addEdu_statement(Edu_statement edu_statement) {
        this.edu_statements.add(edu_statement);
    }

}