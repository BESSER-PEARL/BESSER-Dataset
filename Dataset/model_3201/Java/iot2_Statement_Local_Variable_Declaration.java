





import java.util.List;
import java.util.ArrayList;

public class iot2_Statement_Local_Variable_Declaration extends Statement {

    private String variableNames;





    private List<iot2_Expression> iot2_expressions;


    public iot2_Statement_Local_Variable_Declaration(
        String variableNames    ) {
        super(
        );
        this.variableNames = variableNames;
        this.iot2_expressions = new ArrayList<>();
    }

    public iot2_Statement_Local_Variable_Declaration(
        String variableNames        ArrayList<iot2_Expression> iot2_expressions    ) {
        this.variableNames = variableNames;
        this.iot2_expressions = iot2_expressions;
    }

    public String getVariablenames() {
        return variableNames;
    }

    public void setVariablenames(String variableNames) {
        this.variableNames = variableNames;
    }

    public List<iot2_Expression> getIot2_expressions() {
        return iot2_expressions;
    }

    public void addIot2_expression(Iot2_expression iot2_expression) {
        this.iot2_expressions.add(iot2_expression);
    }

}