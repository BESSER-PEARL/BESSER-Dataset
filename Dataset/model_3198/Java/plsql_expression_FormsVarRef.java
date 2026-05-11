





import java.util.List;
import java.util.ArrayList;

public class plsql_expression_FormsVarRef extends VarRefExpression {

    private String reference;



    public plsql_expression_FormsVarRef(
        String reference    ) {
        super(
        );
        this.reference = reference;
    }


    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }


}