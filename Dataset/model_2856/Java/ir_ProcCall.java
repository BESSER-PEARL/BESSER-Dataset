





import java.util.List;
import java.util.ArrayList;

public class ir_ProcCall extends Statement {






    private ir_Declaration ir_declaration;




    private List<ir_Expression> ir_expressions;




    private List<ir_VariableReference> ir_variablereferences;


    public ir_ProcCall(
    ) {
        super(
        );
        this.ir_expressions = new ArrayList<>();
        this.ir_variablereferences = new ArrayList<>();
    }

    public ir_ProcCall(
        ArrayList<ir_Expression> ir_expressions,        ArrayList<ir_VariableReference> ir_variablereferences    ) {
        this.ir_expressions = ir_expressions;
        this.ir_variablereferences = ir_variablereferences;
    }


    public ir_Declaration getIr_declaration() {
        return ir_declaration;
    }

    public void setIr_declaration(ir_Declaration ir_declaration) {
        this.ir_declaration = ir_declaration;
    }
    public List<ir_Expression> getIr_expressions() {
        return ir_expressions;
    }

    public void addIr_expression(Ir_expression ir_expression) {
        this.ir_expressions.add(ir_expression);
    }
    public List<ir_VariableReference> getIr_variablereferences() {
        return ir_variablereferences;
    }

    public void addIr_variablereference(Ir_variablereference ir_variablereference) {
        this.ir_variablereferences.add(ir_variablereference);
    }

}