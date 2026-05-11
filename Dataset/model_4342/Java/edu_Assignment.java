





import java.util.List;
import java.util.ArrayList;

public class edu_Assignment extends Statement {






    private edu_VariableReference edu_variablereference;




    private edu_Expression edu_expression;


    public edu_Assignment(
    ) {
        super(
        );
    }



    public edu_VariableReference getEdu_variablereference() {
        return edu_variablereference;
    }

    public void setEdu_variablereference(edu_VariableReference edu_variablereference) {
        this.edu_variablereference = edu_variablereference;
    }
    public edu_Expression getEdu_expression() {
        return edu_expression;
    }

    public void setEdu_expression(edu_Expression edu_expression) {
        this.edu_expression = edu_expression;
    }

}