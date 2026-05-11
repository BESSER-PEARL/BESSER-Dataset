





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_Start extends statements_Statement, statements_ErrorHandled {






    private Negate negate;




    private RelationalOperator relationaloperator;


    public cobol_statements_Start(
    ) {
        super(
        );
    }



    public Negate getNegate() {
        return negate;
    }

    public void setNegate(Negate negate) {
        this.negate = negate;
    }
    public RelationalOperator getRelationaloperator() {
        return relationaloperator;
    }

    public void setRelationaloperator(RelationalOperator relationaloperator) {
        this.relationaloperator = relationaloperator;
    }

}