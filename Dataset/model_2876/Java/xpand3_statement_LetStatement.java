





import java.util.List;
import java.util.ArrayList;

public class xpand3_statement_LetStatement extends AbstractStatementWithBody {






    private statement_xpand3_Identifier statement_xpand3_identifier;




    private AbstractExpression abstractexpression;


    public xpand3_statement_LetStatement(
    ) {
        super(
        );
    }



    public statement_xpand3_Identifier getStatement_xpand3_identifier() {
        return statement_xpand3_identifier;
    }

    public void setStatement_xpand3_identifier(statement_xpand3_Identifier statement_xpand3_identifier) {
        this.statement_xpand3_identifier = statement_xpand3_identifier;
    }
    public AbstractExpression getAbstractexpression() {
        return abstractexpression;
    }

    public void setAbstractexpression(AbstractExpression abstractexpression) {
        this.abstractexpression = abstractexpression;
    }

}