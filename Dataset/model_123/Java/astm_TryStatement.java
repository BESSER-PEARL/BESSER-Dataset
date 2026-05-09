





import java.util.List;
import java.util.ArrayList;

public class astm_TryStatement extends Statement {






    private astm_Statement astm_statement;




    private astm_Statement astm_statement;




    private List<astm_CatchBlock> astm_catchblocks;


    public astm_TryStatement(
    ) {
        super(
        );
        this.astm_catchblocks = new ArrayList<>();
    }

    public astm_TryStatement(
        ArrayList<astm_CatchBlock> astm_catchblocks    ) {
        this.astm_catchblocks = astm_catchblocks;
    }


    public astm_Statement getAstm_statement() {
        return astm_statement;
    }

    public void setAstm_statement(astm_Statement astm_statement) {
        this.astm_statement = astm_statement;
    }
    public astm_Statement getAstm_statement() {
        return astm_statement;
    }

    public void setAstm_statement(astm_Statement astm_statement) {
        this.astm_statement = astm_statement;
    }
    public List<astm_CatchBlock> getAstm_catchblocks() {
        return astm_catchblocks;
    }

    public void addAstm_catchblock(Astm_catchblock astm_catchblock) {
        this.astm_catchblocks.add(astm_catchblock);
    }

}