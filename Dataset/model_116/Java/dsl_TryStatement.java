





import java.util.List;
import java.util.ArrayList;

public class dsl_TryStatement  {






    private dsl_Statement dsl_statement;




    private List<dsl_Block> dsl_blocks;




    private List<dsl_FormalParameter> dsl_formalparameters;




    private dsl_Block dsl_block;


    public dsl_TryStatement(
    ) {
        this.dsl_blocks = new ArrayList<>();
        this.dsl_formalparameters = new ArrayList<>();
    }

    public dsl_TryStatement(
        ArrayList<dsl_Block> dsl_blocks,        ArrayList<dsl_FormalParameter> dsl_formalparameters    ) {
        this.dsl_blocks = dsl_blocks;
        this.dsl_formalparameters = dsl_formalparameters;
    }


    public dsl_Statement getDsl_statement() {
        return dsl_statement;
    }

    public void setDsl_statement(dsl_Statement dsl_statement) {
        this.dsl_statement = dsl_statement;
    }
    public List<dsl_Block> getDsl_blocks() {
        return dsl_blocks;
    }

    public void addDsl_block(Dsl_block dsl_block) {
        this.dsl_blocks.add(dsl_block);
    }
    public List<dsl_FormalParameter> getDsl_formalparameters() {
        return dsl_formalparameters;
    }

    public void addDsl_formalparameter(Dsl_formalparameter dsl_formalparameter) {
        this.dsl_formalparameters.add(dsl_formalparameter);
    }
    public dsl_Block getDsl_block() {
        return dsl_block;
    }

    public void setDsl_block(dsl_Block dsl_block) {
        this.dsl_block = dsl_block;
    }

}