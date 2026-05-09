





import java.util.List;
import java.util.ArrayList;

public class JDTAST_TryStatement extends Statement {






    private JDTAST_Block jdtast_block;




    private JDTAST_Block jdtast_block;




    private List<JDTAST_CatchClause> jdtast_catchclauses;


    public JDTAST_TryStatement(
    ) {
        super(
        );
        this.jdtast_catchclauses = new ArrayList<>();
    }

    public JDTAST_TryStatement(
        ArrayList<JDTAST_CatchClause> jdtast_catchclauses    ) {
        this.jdtast_catchclauses = jdtast_catchclauses;
    }


    public JDTAST_Block getJdtast_block() {
        return jdtast_block;
    }

    public void setJdtast_block(JDTAST_Block jdtast_block) {
        this.jdtast_block = jdtast_block;
    }
    public JDTAST_Block getJdtast_block() {
        return jdtast_block;
    }

    public void setJdtast_block(JDTAST_Block jdtast_block) {
        this.jdtast_block = jdtast_block;
    }
    public List<JDTAST_CatchClause> getJdtast_catchclauses() {
        return jdtast_catchclauses;
    }

    public void addJdtast_catchclause(Jdtast_catchclause jdtast_catchclause) {
        this.jdtast_catchclauses.add(jdtast_catchclause);
    }

}