





import java.util.List;
import java.util.ArrayList;

public class transformation_Invocation extends Expression {






    private transformation_Expression transformation_expression;




    private List<transformation_Expression> transformation_expressions;


    public transformation_Invocation(
    ) {
        super(
        );
        this.transformation_expressions = new ArrayList<>();
    }

    public transformation_Invocation(
        ArrayList<transformation_Expression> transformation_expressions    ) {
        this.transformation_expressions = transformation_expressions;
    }


    public transformation_Expression getTransformation_expression() {
        return transformation_expression;
    }

    public void setTransformation_expression(transformation_Expression transformation_expression) {
        this.transformation_expression = transformation_expression;
    }
    public List<transformation_Expression> getTransformation_expressions() {
        return transformation_expressions;
    }

    public void addTransformation_expression(Transformation_expression transformation_expression) {
        this.transformation_expressions.add(transformation_expression);
    }

}