





import java.util.List;
import java.util.ArrayList;

public class edu_ArrayLiteral extends Literal {






    private List<edu_Expression> edu_expressions;


    public edu_ArrayLiteral(
    ) {
        super(
        );
        this.edu_expressions = new ArrayList<>();
    }

    public edu_ArrayLiteral(
        ArrayList<edu_Expression> edu_expressions    ) {
        this.edu_expressions = edu_expressions;
    }


    public List<edu_Expression> getEdu_expressions() {
        return edu_expressions;
    }

    public void addEdu_expression(Edu_expression edu_expression) {
        this.edu_expressions.add(edu_expression);
    }

}