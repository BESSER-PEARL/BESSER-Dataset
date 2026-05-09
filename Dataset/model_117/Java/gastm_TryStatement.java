





import java.util.List;
import java.util.ArrayList;

public class gastm_TryStatement extends Statement {






    private List<gastm_CatchBlock> gastm_catchblocks;




    private gastm_Statement gastm_statement;




    private gastm_Statement gastm_statement;


    public gastm_TryStatement(
    ) {
        super(
        );
        this.gastm_catchblocks = new ArrayList<>();
    }

    public gastm_TryStatement(
        ArrayList<gastm_CatchBlock> gastm_catchblocks    ) {
        this.gastm_catchblocks = gastm_catchblocks;
    }


    public List<gastm_CatchBlock> getGastm_catchblocks() {
        return gastm_catchblocks;
    }

    public void addGastm_catchblock(Gastm_catchblock gastm_catchblock) {
        this.gastm_catchblocks.add(gastm_catchblock);
    }
    public gastm_Statement getGastm_statement() {
        return gastm_statement;
    }

    public void setGastm_statement(gastm_Statement gastm_statement) {
        this.gastm_statement = gastm_statement;
    }
    public gastm_Statement getGastm_statement() {
        return gastm_statement;
    }

    public void setGastm_statement(gastm_Statement gastm_statement) {
        this.gastm_statement = gastm_statement;
    }

}