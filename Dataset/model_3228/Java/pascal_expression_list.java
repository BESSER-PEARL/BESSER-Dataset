





import java.util.List;
import java.util.ArrayList;

public class pascal_expression_list  {






    private List<pascal_expression> pascal_expressions;




    private pascal_function_designator pascal_function_designator;




    private pascal_set pascal_set;




    private pascal_resto pascal_resto;


    public pascal_expression_list(
    ) {
        this.pascal_expressions = new ArrayList<>();
    }

    public pascal_expression_list(
        ArrayList<pascal_expression> pascal_expressions    ) {
        this.pascal_expressions = pascal_expressions;
    }


    public List<pascal_expression> getPascal_expressions() {
        return pascal_expressions;
    }

    public void addPascal_expression(Pascal_expression pascal_expression) {
        this.pascal_expressions.add(pascal_expression);
    }
    public pascal_function_designator getPascal_function_designator() {
        return pascal_function_designator;
    }

    public void setPascal_function_designator(pascal_function_designator pascal_function_designator) {
        this.pascal_function_designator = pascal_function_designator;
    }
    public pascal_set getPascal_set() {
        return pascal_set;
    }

    public void setPascal_set(pascal_set pascal_set) {
        this.pascal_set = pascal_set;
    }
    public pascal_resto getPascal_resto() {
        return pascal_resto;
    }

    public void setPascal_resto(pascal_resto pascal_resto) {
        this.pascal_resto = pascal_resto;
    }

}