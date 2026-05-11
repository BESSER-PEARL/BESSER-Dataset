





import java.util.List;
import java.util.ArrayList;

public class xpand3_statement_FileStatement extends AbstractStatementWithBody {

    private boolean once;





    private AbstractExpression abstractexpression;




    private statement_xpand3_Identifier statement_xpand3_identifier;


    public xpand3_statement_FileStatement(
        boolean once    ) {
        super(
        );
        this.once = once;
    }


    public boolean getOnce() {
        return once;
    }

    public void setOnce(boolean once) {
        this.once = once;
    }

    public AbstractExpression getAbstractexpression() {
        return abstractexpression;
    }

    public void setAbstractexpression(AbstractExpression abstractexpression) {
        this.abstractexpression = abstractexpression;
    }
    public statement_xpand3_Identifier getStatement_xpand3_identifier() {
        return statement_xpand3_identifier;
    }

    public void setStatement_xpand3_identifier(statement_xpand3_Identifier statement_xpand3_identifier) {
        this.statement_xpand3_identifier = statement_xpand3_identifier;
    }

}