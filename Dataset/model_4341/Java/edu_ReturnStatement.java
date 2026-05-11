





import java.util.List;
import java.util.ArrayList;

public class edu_ReturnStatement extends Statement {






    private edu_FunctionDeclaration edu_functiondeclaration;




    private edu_Expression edu_expression;


    public edu_ReturnStatement(
    ) {
        super(
        );
    }



    public edu_FunctionDeclaration getEdu_functiondeclaration() {
        return edu_functiondeclaration;
    }

    public void setEdu_functiondeclaration(edu_FunctionDeclaration edu_functiondeclaration) {
        this.edu_functiondeclaration = edu_functiondeclaration;
    }
    public edu_Expression getEdu_expression() {
        return edu_expression;
    }

    public void setEdu_expression(edu_Expression edu_expression) {
        this.edu_expression = edu_expression;
    }

}