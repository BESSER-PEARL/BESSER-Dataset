





import java.util.List;
import java.util.ArrayList;

public class cst_IfBlock extends Block {






    private cst_ModelExpression cst_modelexpression;




    private cst_Block cst_block;




    private cst_IfBlock cst_ifblock;


    public cst_IfBlock(
    ) {
        super(
        );
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
    public cst_IfBlock getCst_ifblock() {
        return cst_ifblock;
    }

    public void setCst_ifblock(cst_IfBlock cst_ifblock) {
        this.cst_ifblock = cst_ifblock;
    }

}