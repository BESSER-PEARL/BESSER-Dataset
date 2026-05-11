





import java.util.List;
import java.util.ArrayList;

public class expressions_Model  {






    private List<expressions_Function> expressions_functions;


    public expressions_Model(
    ) {
        this.expressions_functions = new ArrayList<>();
    }

    public expressions_Model(
        ArrayList<expressions_Function> expressions_functions    ) {
        this.expressions_functions = expressions_functions;
    }


    public List<expressions_Function> getExpressions_functions() {
        return expressions_functions;
    }

    public void addExpressions_function(Expressions_function expressions_function) {
        this.expressions_functions.add(expressions_function);
    }

}