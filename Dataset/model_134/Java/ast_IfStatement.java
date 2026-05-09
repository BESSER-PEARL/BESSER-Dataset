





import java.util.List;
import java.util.ArrayList;

public class ast_IfStatement extends MethodContentStatement {






    private ast_MethodBlock ast_methodblock;




    private List<ast_IfThenPart> ast_ifthenparts;


    public ast_IfStatement(
    ) {
        super(
        );
        this.ast_ifthenparts = new ArrayList<>();
    }

    public ast_IfStatement(
        ArrayList<ast_IfThenPart> ast_ifthenparts    ) {
        this.ast_ifthenparts = ast_ifthenparts;
    }


    public ast_MethodBlock getAst_methodblock() {
        return ast_methodblock;
    }

    public void setAst_methodblock(ast_MethodBlock ast_methodblock) {
        this.ast_methodblock = ast_methodblock;
    }
    public List<ast_IfThenPart> getAst_ifthenparts() {
        return ast_ifthenparts;
    }

    public void addAst_ifthenpart(Ast_ifthenpart ast_ifthenpart) {
        this.ast_ifthenparts.add(ast_ifthenpart);
    }

}