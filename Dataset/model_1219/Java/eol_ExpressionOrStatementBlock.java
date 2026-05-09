





import java.util.List;
import java.util.ArrayList;

public class eol_ExpressionOrStatementBlock extends EolElement {






    private eol_TransactionStatement eol_transactionstatement;




    private eol_Block eol_block;


    public eol_ExpressionOrStatementBlock(
    ) {
        super(
        );
    }



    public eol_TransactionStatement getEol_transactionstatement() {
        return eol_transactionstatement;
    }

    public void setEol_transactionstatement(eol_TransactionStatement eol_transactionstatement) {
        this.eol_transactionstatement = eol_transactionstatement;
    }
    public eol_Block getEol_block() {
        return eol_block;
    }

    public void setEol_block(eol_Block eol_block) {
        this.eol_block = eol_block;
    }

}