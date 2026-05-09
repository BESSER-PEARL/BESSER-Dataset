





import java.util.List;
import java.util.ArrayList;

public class astm_BlockScope extends Scope {






    private astm_BlockStatement astm_blockstatement;


    public astm_BlockScope(
    ) {
        super(
        );
    }



    public astm_BlockStatement getAstm_blockstatement() {
        return astm_blockstatement;
    }

    public void setAstm_blockstatement(astm_BlockStatement astm_blockstatement) {
        this.astm_blockstatement = astm_blockstatement;
    }

}