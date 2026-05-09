





import java.util.List;
import java.util.ArrayList;

public class astm_DataDefinition extends Definition {

    private boolean isMutable;





    private astm_Expression astm_expression;


    public astm_DataDefinition(
        boolean isMutable    ) {
        super(
        );
        this.isMutable = isMutable;
    }


    public boolean getIsmutable() {
        return isMutable;
    }

    public void setIsmutable(boolean isMutable) {
        this.isMutable = isMutable;
    }

    public astm_Expression getAstm_expression() {
        return astm_expression;
    }

    public void setAstm_expression(astm_Expression astm_expression) {
        this.astm_expression = astm_expression;
    }

}