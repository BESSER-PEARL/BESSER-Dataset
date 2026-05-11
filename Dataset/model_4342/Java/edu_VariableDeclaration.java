





import java.util.List;
import java.util.ArrayList;

public class edu_VariableDeclaration extends Statement {

    private String name;





    private edu_Expression edu_expression;




    private edu_QuantifiedExpression edu_quantifiedexpression;




    private edu_FunctionDeclaration edu_functiondeclaration;




    private edu_LetExpression edu_letexpression;




    private edu_Type edu_type;




    private edu_VariableReference edu_variablereference;


    public edu_VariableDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public edu_Expression getEdu_expression() {
        return edu_expression;
    }

    public void setEdu_expression(edu_Expression edu_expression) {
        this.edu_expression = edu_expression;
    }
    public edu_QuantifiedExpression getEdu_quantifiedexpression() {
        return edu_quantifiedexpression;
    }

    public void setEdu_quantifiedexpression(edu_QuantifiedExpression edu_quantifiedexpression) {
        this.edu_quantifiedexpression = edu_quantifiedexpression;
    }
    public edu_FunctionDeclaration getEdu_functiondeclaration() {
        return edu_functiondeclaration;
    }

    public void setEdu_functiondeclaration(edu_FunctionDeclaration edu_functiondeclaration) {
        this.edu_functiondeclaration = edu_functiondeclaration;
    }
    public edu_LetExpression getEdu_letexpression() {
        return edu_letexpression;
    }

    public void setEdu_letexpression(edu_LetExpression edu_letexpression) {
        this.edu_letexpression = edu_letexpression;
    }
    public edu_Type getEdu_type() {
        return edu_type;
    }

    public void setEdu_type(edu_Type edu_type) {
        this.edu_type = edu_type;
    }
    public edu_VariableReference getEdu_variablereference() {
        return edu_variablereference;
    }

    public void setEdu_variablereference(edu_VariableReference edu_variablereference) {
        this.edu_variablereference = edu_variablereference;
    }

}