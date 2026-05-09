





import java.util.List;
import java.util.ArrayList;

public class eol_TransactionStatement extends Statement {






    private List<eol_NameExpression> eol_nameexpressions;




    private eol_Block eol_block;


    public eol_TransactionStatement(
    ) {
        super(
        );
        this.eol_nameexpressions = new ArrayList<>();
    }

    public eol_TransactionStatement(
        ArrayList<eol_NameExpression> eol_nameexpressions    ) {
        this.eol_nameexpressions = eol_nameexpressions;
    }


    public List<eol_NameExpression> getEol_nameexpressions() {
        return eol_nameexpressions;
    }

    public void addEol_nameexpression(Eol_nameexpression eol_nameexpression) {
        this.eol_nameexpressions.add(eol_nameexpression);
    }
    public eol_Block getEol_block() {
        return eol_block;
    }

    public void setEol_block(eol_Block eol_block) {
        this.eol_block = eol_block;
    }

}