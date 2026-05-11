





import java.util.List;
import java.util.ArrayList;

public class core_IfBranch  {






    private core_Expression core_expression;




    private core_IfExpr core_ifexpr;




    private core_IfExpr core_ifexpr;




    private List<core_Statement> core_statements;




    private core_IfExpr core_ifexpr;


    public core_IfBranch(
    ) {
        this.core_statements = new ArrayList<>();
    }

    public core_IfBranch(
        ArrayList<core_Statement> core_statements    ) {
        this.core_statements = core_statements;
    }


    public core_Expression getCore_expression() {
        return core_expression;
    }

    public void setCore_expression(core_Expression core_expression) {
        this.core_expression = core_expression;
    }
    public core_IfExpr getCore_ifexpr() {
        return core_ifexpr;
    }

    public void setCore_ifexpr(core_IfExpr core_ifexpr) {
        this.core_ifexpr = core_ifexpr;
    }
    public core_IfExpr getCore_ifexpr() {
        return core_ifexpr;
    }

    public void setCore_ifexpr(core_IfExpr core_ifexpr) {
        this.core_ifexpr = core_ifexpr;
    }
    public List<core_Statement> getCore_statements() {
        return core_statements;
    }

    public void addCore_statement(Core_statement core_statement) {
        this.core_statements.add(core_statement);
    }
    public core_IfExpr getCore_ifexpr() {
        return core_ifexpr;
    }

    public void setCore_ifexpr(core_IfExpr core_ifexpr) {
        this.core_ifexpr = core_ifexpr;
    }

}