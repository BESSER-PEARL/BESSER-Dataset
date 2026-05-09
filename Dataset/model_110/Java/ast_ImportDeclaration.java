





import java.util.List;
import java.util.ArrayList;

public class ast_ImportDeclaration extends ASTNode {

    private boolean onDemand;
    private boolean static;





    private ast_Name ast_name;


    public ast_ImportDeclaration(
        boolean onDemand,        boolean static    ) {
        super(
        );
        this.onDemand = onDemand;
        this.static = static;
    }


    public boolean getOndemand() {
        return onDemand;
    }

    public void setOndemand(boolean onDemand) {
        this.onDemand = onDemand;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public ast_Name getAst_name() {
        return ast_name;
    }

    public void setAst_name(ast_Name ast_name) {
        this.ast_name = ast_name;
    }

}