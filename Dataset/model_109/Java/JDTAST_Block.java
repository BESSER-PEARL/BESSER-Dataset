





import java.util.List;
import java.util.ArrayList;

public class JDTAST_Block extends Statement {






    private JDTAST_CatchClause jdtast_catchclause;




    private List<JDTAST_Statement> jdtast_statements;


    public JDTAST_Block(
    ) {
        super(
        );
        this.jdtast_statements = new ArrayList<>();
    }

    public JDTAST_Block(
        ArrayList<JDTAST_Statement> jdtast_statements    ) {
        this.jdtast_statements = jdtast_statements;
    }


    public JDTAST_CatchClause getJdtast_catchclause() {
        return jdtast_catchclause;
    }

    public void setJdtast_catchclause(JDTAST_CatchClause jdtast_catchclause) {
        this.jdtast_catchclause = jdtast_catchclause;
    }
    public List<JDTAST_Statement> getJdtast_statements() {
        return jdtast_statements;
    }

    public void addJdtast_statement(Jdtast_statement jdtast_statement) {
        this.jdtast_statements.add(jdtast_statement);
    }

}