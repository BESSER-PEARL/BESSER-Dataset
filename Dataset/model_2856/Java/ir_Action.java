





import java.util.List;
import java.util.ArrayList;

public class ir_Action extends Scope {

    private String tag;





    private List<ir_Statement> ir_statements;


    public ir_Action(
        String tag    ) {
        super(
        );
        this.tag = tag;
        this.ir_statements = new ArrayList<>();
    }

    public ir_Action(
        String tag        ArrayList<ir_Statement> ir_statements    ) {
        this.tag = tag;
        this.ir_statements = ir_statements;
    }

    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }

    public List<ir_Statement> getIr_statements() {
        return ir_statements;
    }

    public void addIr_statement(Ir_statement ir_statement) {
        this.ir_statements.add(ir_statement);
    }

}