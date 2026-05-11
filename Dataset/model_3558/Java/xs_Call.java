





import java.util.List;
import java.util.ArrayList;

public class xs_Call extends Expression {






    private List<xs_Expression> xs_expressions;




    private xs_FunctionDeclaration xs_functiondeclaration;


    public xs_Call(
    ) {
        super(
        );
        this.xs_expressions = new ArrayList<>();
    }

    public xs_Call(
        ArrayList<xs_Expression> xs_expressions    ) {
        this.xs_expressions = xs_expressions;
    }


    public List<xs_Expression> getXs_expressions() {
        return xs_expressions;
    }

    public void addXs_expression(Xs_expression xs_expression) {
        this.xs_expressions.add(xs_expression);
    }
    public xs_FunctionDeclaration getXs_functiondeclaration() {
        return xs_functiondeclaration;
    }

    public void setXs_functiondeclaration(xs_FunctionDeclaration xs_functiondeclaration) {
        this.xs_functiondeclaration = xs_functiondeclaration;
    }

}