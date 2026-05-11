





import java.util.List;
import java.util.ArrayList;

public class Model_SimplePredicate extends Predicate {

    private String operator;





    private Model_Variable model_variable;


    public Model_SimplePredicate(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public Model_Variable getModel_variable() {
        return model_variable;
    }

    public void setModel_variable(Model_Variable model_variable) {
        this.model_variable = model_variable;
    }

}