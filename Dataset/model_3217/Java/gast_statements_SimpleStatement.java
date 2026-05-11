





import java.util.List;
import java.util.ArrayList;

public class gast_statements_SimpleStatement extends statements_Statement, statements_FlowInstr {






    private GASTExpression gastexpression;


    public gast_statements_SimpleStatement(
    ) {
        super(
        );
    }



    public GASTExpression getGastexpression() {
        return gastexpression;
    }

    public void setGastexpression(GASTExpression gastexpression) {
        this.gastexpression = gastexpression;
    }

}