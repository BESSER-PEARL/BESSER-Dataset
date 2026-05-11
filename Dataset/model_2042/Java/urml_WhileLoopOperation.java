





import java.util.List;
import java.util.ArrayList;

public class urml_WhileLoopOperation extends StatementOperation {






    private List<urml_StatementOperation> urml_statementoperations;




    private urml_Expression urml_expression;


    public urml_WhileLoopOperation(
    ) {
        super(
        );
        this.urml_statementoperations = new ArrayList<>();
    }

    public urml_WhileLoopOperation(
        ArrayList<urml_StatementOperation> urml_statementoperations    ) {
        this.urml_statementoperations = urml_statementoperations;
    }


    public List<urml_StatementOperation> getUrml_statementoperations() {
        return urml_statementoperations;
    }

    public void addUrml_statementoperation(Urml_statementoperation urml_statementoperation) {
        this.urml_statementoperations.add(urml_statementoperation);
    }
    public urml_Expression getUrml_expression() {
        return urml_expression;
    }

    public void setUrml_expression(urml_Expression urml_expression) {
        this.urml_expression = urml_expression;
    }

}