





import java.util.List;
import java.util.ArrayList;

public class edu_FunctionCall extends Expression {






    private List<edu_Expression> edu_expressions;




    private edu_FunctionDeclaration edu_functiondeclaration;


    public edu_FunctionCall(
    ) {
        super(
        );
        this.edu_expressions = new ArrayList<>();
    }

    public edu_FunctionCall(
        ArrayList<edu_Expression> edu_expressions    ) {
        this.edu_expressions = edu_expressions;
    }


    public List<edu_Expression> getEdu_expressions() {
        return edu_expressions;
    }

    public void addEdu_expression(Edu_expression edu_expression) {
        this.edu_expressions.add(edu_expression);
    }
    public edu_FunctionDeclaration getEdu_functiondeclaration() {
        return edu_functiondeclaration;
    }

    public void setEdu_functiondeclaration(edu_FunctionDeclaration edu_functiondeclaration) {
        this.edu_functiondeclaration = edu_functiondeclaration;
    }

}