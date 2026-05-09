





import java.util.List;
import java.util.ArrayList;

public class cst_IfBlock extends Block {






    private List<cst_IfBlock> cst_ifblocks;




    private cst_ModelExpression cst_modelexpression;




    private cst_Block cst_block;


    public cst_IfBlock(
    ) {
        super(
        );
        this.cst_ifblocks = new ArrayList<>();
    }

    public cst_IfBlock(
        ArrayList<cst_IfBlock> cst_ifblocks    ) {
        this.cst_ifblocks = cst_ifblocks;
    }


    public List<cst_IfBlock> getCst_ifblocks() {
        return cst_ifblocks;
    }

    public void addCst_ifblock(Cst_ifblock cst_ifblock) {
        this.cst_ifblocks.add(cst_ifblock);
    }
    public cst_ModelExpression getCst_modelexpression() {
        return cst_modelexpression;
    }

    public void setCst_modelexpression(cst_ModelExpression cst_modelexpression) {
        this.cst_modelexpression = cst_modelexpression;
    }
    public cst_Block getCst_block() {
        return cst_block;
    }

    public void setCst_block(cst_Block cst_block) {
        this.cst_block = cst_block;
    }

}