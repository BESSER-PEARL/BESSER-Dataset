





import java.util.List;
import java.util.ArrayList;

public class gastm_BlockStatement extends Statement {






    private List<gastm_Statement> gastm_statements;




    private gastm_BlockScope gastm_blockscope;


    public gastm_BlockStatement(
    ) {
        super(
        );
        this.gastm_statements = new ArrayList<>();
    }

    public gastm_BlockStatement(
        ArrayList<gastm_Statement> gastm_statements    ) {
        this.gastm_statements = gastm_statements;
    }


    public List<gastm_Statement> getGastm_statements() {
        return gastm_statements;
    }

    public void addGastm_statement(Gastm_statement gastm_statement) {
        this.gastm_statements.add(gastm_statement);
    }
    public gastm_BlockScope getGastm_blockscope() {
        return gastm_blockscope;
    }

    public void setGastm_blockscope(gastm_BlockScope gastm_blockscope) {
        this.gastm_blockscope = gastm_blockscope;
    }

}