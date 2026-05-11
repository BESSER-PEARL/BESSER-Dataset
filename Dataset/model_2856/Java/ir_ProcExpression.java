





import java.util.List;
import java.util.ArrayList;

public class ir_ProcExpression extends Scope, Expression {






    private List<ir_Variable> ir_variables;




    private List<ir_Variable> ir_variables;


    public ir_ProcExpression(
    ) {
        super(
        );
        this.ir_variables = new ArrayList<>();
        this.ir_variables = new ArrayList<>();
    }

    public ir_ProcExpression(
        ArrayList<ir_Variable> ir_variables,        ArrayList<ir_Variable> ir_variables    ) {
        this.ir_variables = ir_variables;
        this.ir_variables = ir_variables;
    }


    public List<ir_Variable> getIr_variables() {
        return ir_variables;
    }

    public void addIr_variable(Ir_variable ir_variable) {
        this.ir_variables.add(ir_variable);
    }
    public List<ir_Variable> getIr_variables() {
        return ir_variables;
    }

    public void addIr_variable(Ir_variable ir_variable) {
        this.ir_variables.add(ir_variable);
    }

}