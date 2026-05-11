





import java.util.List;
import java.util.ArrayList;

public class pascal_expression extends output_value {

    private String relational_operator;





    private pascal_actual_value pascal_actual_value;




    private List<pascal_expression> pascal_expressions;


    public pascal_expression(
        String relational_operator    ) {
        super(
        );
        this.relational_operator = relational_operator;
        this.pascal_expressions = new ArrayList<>();
    }

    public pascal_expression(
        String relational_operator        ArrayList<pascal_expression> pascal_expressions    ) {
        this.relational_operator = relational_operator;
        this.pascal_expressions = pascal_expressions;
    }

    public String getRelational_operator() {
        return relational_operator;
    }

    public void setRelational_operator(String relational_operator) {
        this.relational_operator = relational_operator;
    }

    public pascal_actual_value getPascal_actual_value() {
        return pascal_actual_value;
    }

    public void setPascal_actual_value(pascal_actual_value pascal_actual_value) {
        this.pascal_actual_value = pascal_actual_value;
    }
    public List<pascal_expression> getPascal_expressions() {
        return pascal_expressions;
    }

    public void addPascal_expression(Pascal_expression pascal_expression) {
        this.pascal_expressions.add(pascal_expression);
    }

}