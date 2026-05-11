





import java.util.List;
import java.util.ArrayList;

public class ir_Block extends Scope, Statement {






    private List<ir_Statement> ir_statements;




    private ir_ProcExpression ir_procexpression;


    public ir_Block(
    ) {
        super(
        );
        this.ir_statements = new ArrayList<>();
    }

    public ir_Block(
        ArrayList<ir_Statement> ir_statements    ) {
        this.ir_statements = ir_statements;
    }


    public List<ir_Statement> getIr_statements() {
        return ir_statements;
    }

    public void addIr_statement(Ir_statement ir_statement) {
        this.ir_statements.add(ir_statement);
    }
    public ir_ProcExpression getIr_procexpression() {
        return ir_procexpression;
    }

    public void setIr_procexpression(ir_ProcExpression ir_procexpression) {
        this.ir_procexpression = ir_procexpression;
    }

}