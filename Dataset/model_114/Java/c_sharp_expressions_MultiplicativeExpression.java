





import java.util.List;
import java.util.ArrayList;

public class c_sharp_expressions_MultiplicativeExpression  {






    private List<UnaryExpression> unaryexpressions;




    private Multiplication multiplication;


    public c_sharp_expressions_MultiplicativeExpression(
    ) {
        this.unaryexpressions = new ArrayList<>();
    }

    public c_sharp_expressions_MultiplicativeExpression(
        ArrayList<UnaryExpression> unaryexpressions    ) {
        this.unaryexpressions = unaryexpressions;
    }


    public List<UnaryExpression> getUnaryexpressions() {
        return unaryexpressions;
    }

    public void addUnaryexpression(Unaryexpression unaryexpression) {
        this.unaryexpressions.add(unaryexpression);
    }
    public Multiplication getMultiplication() {
        return multiplication;
    }

    public void setMultiplication(Multiplication multiplication) {
        this.multiplication = multiplication;
    }

}