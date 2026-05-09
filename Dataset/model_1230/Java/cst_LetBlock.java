





import java.util.List;
import java.util.ArrayList;

public class cst_LetBlock extends Block {






    private cst_Variable cst_variable;




    private List<cst_LetBlock> cst_letblocks;




    private cst_Block cst_block;


    public cst_LetBlock(
    ) {
        super(
        );
        this.cst_letblocks = new ArrayList<>();
    }

    public cst_LetBlock(
        ArrayList<cst_LetBlock> cst_letblocks    ) {
        this.cst_letblocks = cst_letblocks;
    }


    public cst_Variable getCst_variable() {
        return cst_variable;
    }

    public void setCst_variable(cst_Variable cst_variable) {
        this.cst_variable = cst_variable;
    }
    public List<cst_LetBlock> getCst_letblocks() {
        return cst_letblocks;
    }

    public void addCst_letblock(Cst_letblock cst_letblock) {
        this.cst_letblocks.add(cst_letblock);
    }
    public cst_Block getCst_block() {
        return cst_block;
    }

    public void setCst_block(cst_Block cst_block) {
        this.cst_block = cst_block;
    }

}