





import java.util.List;
import java.util.ArrayList;

public class cst_LetBlock extends Block {






    private cst_Variable cst_variable;




    private cst_Block cst_block;




    private cst_LetBlock cst_letblock;


    public cst_LetBlock(
    ) {
        super(
        );
    }



    public cst_Variable getCst_variable() {
        return cst_variable;
    }

    public void setCst_variable(cst_Variable cst_variable) {
        this.cst_variable = cst_variable;
    }
    public cst_Block getCst_block() {
        return cst_block;
    }

    public void setCst_block(cst_Block cst_block) {
        this.cst_block = cst_block;
    }
    public cst_LetBlock getCst_letblock() {
        return cst_letblock;
    }

    public void setCst_letblock(cst_LetBlock cst_letblock) {
        this.cst_letblock = cst_letblock;
    }

}