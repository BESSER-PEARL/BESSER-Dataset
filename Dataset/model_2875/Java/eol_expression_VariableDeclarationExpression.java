





import java.util.List;
import java.util.ArrayList;

public class eol_expression_VariableDeclarationExpression extends Expression {

    private boolean create;



    public eol_expression_VariableDeclarationExpression(
        boolean create    ) {
        super(
        );
        this.create = create;
    }


    public boolean getCreate() {
        return create;
    }

    public void setCreate(boolean create) {
        this.create = create;
    }


}