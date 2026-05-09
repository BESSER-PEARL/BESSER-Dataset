





import java.util.List;
import java.util.ArrayList;

public class ast_TryStatement extends ScopeStatement {






    private ast_MethodBlock ast_methodblock;




    private List<ast_CatchPart> ast_catchparts;


    public ast_TryStatement(
    ) {
        super(
        );
        this.ast_catchparts = new ArrayList<>();
    }

    public ast_TryStatement(
        ArrayList<ast_CatchPart> ast_catchparts    ) {
        this.ast_catchparts = ast_catchparts;
    }


    public ast_MethodBlock getAst_methodblock() {
        return ast_methodblock;
    }

    public void setAst_methodblock(ast_MethodBlock ast_methodblock) {
        this.ast_methodblock = ast_methodblock;
    }
    public List<ast_CatchPart> getAst_catchparts() {
        return ast_catchparts;
    }

    public void addAst_catchpart(Ast_catchpart ast_catchpart) {
        this.ast_catchparts.add(ast_catchpart);
    }

}