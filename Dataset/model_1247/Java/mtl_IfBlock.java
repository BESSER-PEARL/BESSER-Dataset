





import java.util.List;
import java.util.ArrayList;

public class mtl_IfBlock extends Block {






    private mtl_IfBlock mtl_ifblock;




    private mtl_Block mtl_block;




    private OCLExpression oclexpression;


    public mtl_IfBlock(
    ) {
        super(
        );
    }



    public mtl_IfBlock getMtl_ifblock() {
        return mtl_ifblock;
    }

    public void setMtl_ifblock(mtl_IfBlock mtl_ifblock) {
        this.mtl_ifblock = mtl_ifblock;
    }
    public mtl_Block getMtl_block() {
        return mtl_block;
    }

    public void setMtl_block(mtl_Block mtl_block) {
        this.mtl_block = mtl_block;
    }
    public OCLExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OCLExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}