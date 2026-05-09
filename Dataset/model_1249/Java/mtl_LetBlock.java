





import java.util.List;
import java.util.ArrayList;

public class mtl_LetBlock extends Block {






    private Variable variable;




    private mtl_Block mtl_block;




    private List<mtl_LetBlock> mtl_letblocks;


    public mtl_LetBlock(
    ) {
        super(
        );
        this.mtl_letblocks = new ArrayList<>();
    }

    public mtl_LetBlock(
        ArrayList<mtl_LetBlock> mtl_letblocks    ) {
        this.mtl_letblocks = mtl_letblocks;
    }


    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }
    public mtl_Block getMtl_block() {
        return mtl_block;
    }

    public void setMtl_block(mtl_Block mtl_block) {
        this.mtl_block = mtl_block;
    }
    public List<mtl_LetBlock> getMtl_letblocks() {
        return mtl_letblocks;
    }

    public void addMtl_letblock(Mtl_letblock mtl_letblock) {
        this.mtl_letblocks.add(mtl_letblock);
    }

}