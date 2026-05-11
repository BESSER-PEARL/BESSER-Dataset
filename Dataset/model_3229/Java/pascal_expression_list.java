





import java.util.List;
import java.util.ArrayList;

public class pascal_expression_list  {






    private pascal_var_ pascal_var_;




    private pascal_set pascal_set;




    private List<pascal_expression> pascal_expressions;




    private pascal_function_designator pascal_function_designator;


    public pascal_expression_list(
    ) {
        this.pascal_expressions = new ArrayList<>();
    }

    public pascal_expression_list(
        ArrayList<pascal_expression> pascal_expressions    ) {
        this.pascal_expressions = pascal_expressions;
    }


    public pascal_var_ getPascal_var_() {
        return pascal_var_;
    }

    public void setPascal_var_(pascal_var_ pascal_var_) {
        this.pascal_var_ = pascal_var_;
    }
    public pascal_set getPascal_set() {
        return pascal_set;
    }

    public void setPascal_set(pascal_set pascal_set) {
        this.pascal_set = pascal_set;
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

}