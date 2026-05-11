





import java.util.List;
import java.util.ArrayList;

public class urml_Invoke extends StatementOperation, Statement {






    private List<urml_Expression> urml_expressions;




    private urml_Operation urml_operation;


    public urml_Invoke(
    ) {
        super(
        );
        this.urml_expressions = new ArrayList<>();
    }

    public urml_Invoke(
        ArrayList<urml_Expression> urml_expressions    ) {
        this.urml_expressions = urml_expressions;
    }


    public List<urml_Expression> getUrml_expressions() {
        return urml_expressions;
    }

    public void addUrml_expression(Urml_expression urml_expression) {
        this.urml_expressions.add(urml_expression);
    }
    public urml_Operation getUrml_operation() {
        return urml_operation;
    }

    public void setUrml_operation(urml_Operation urml_operation) {
        this.urml_operation = urml_operation;
    }

}