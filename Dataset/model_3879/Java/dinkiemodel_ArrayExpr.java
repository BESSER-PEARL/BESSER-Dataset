





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_ArrayExpr extends Expression {

    private String varName;





    private dinkiemodel_Expression dinkiemodel_expression;


    public dinkiemodel_ArrayExpr(
        String varName    ) {
        super(
        );
        this.varName = varName;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }

    public dinkiemodel_Expression getDinkiemodel_expression() {
        return dinkiemodel_expression;
    }

    public void setDinkiemodel_expression(dinkiemodel_Expression dinkiemodel_expression) {
        this.dinkiemodel_expression = dinkiemodel_expression;
    }

}