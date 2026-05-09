





import java.util.List;
import java.util.ArrayList;

public class DOM_CatchClause extends ASTNode {






    private SingleVariableDeclaration singlevariabledeclaration;




    private Block block;


    public DOM_CatchClause(
    ) {
        super(
        );
    }



    public SingleVariableDeclaration getSinglevariabledeclaration() {
        return singlevariabledeclaration;
    }

    public void setSinglevariabledeclaration(SingleVariableDeclaration singlevariabledeclaration) {
        this.singlevariabledeclaration = singlevariabledeclaration;
    }
    public Block getBlock() {
        return block;
    }

    public void setBlock(Block block) {
        this.block = block;
    }

}