





import java.util.List;
import java.util.ArrayList;

public class ast_MethodBlock extends MethodContentStatement {






    private ast_MethodStatement ast_methodstatement;




    private ast_SwitchPart ast_switchpart;




    private List<ast_MethodContentStatement> ast_methodcontentstatements;




    private ast_CatchPart ast_catchpart;




    private ast_ConstructorStatement ast_constructorstatement;




    private ast_IfThenPart ast_ifthenpart;


    public ast_MethodBlock(
    ) {
        super(
        );
        this.ast_methodcontentstatements = new ArrayList<>();
    }

    public ast_MethodBlock(
        ArrayList<ast_MethodContentStatement> ast_methodcontentstatements    ) {
        this.ast_methodcontentstatements = ast_methodcontentstatements;
    }


    public ast_MethodStatement getAst_methodstatement() {
        return ast_methodstatement;
    }

    public void setAst_methodstatement(ast_MethodStatement ast_methodstatement) {
        this.ast_methodstatement = ast_methodstatement;
    }
    public ast_SwitchPart getAst_switchpart() {
        return ast_switchpart;
    }

    public void setAst_switchpart(ast_SwitchPart ast_switchpart) {
        this.ast_switchpart = ast_switchpart;
    }
    public List<ast_MethodContentStatement> getAst_methodcontentstatements() {
        return ast_methodcontentstatements;
    }

    public void addAst_methodcontentstatement(Ast_methodcontentstatement ast_methodcontentstatement) {
        this.ast_methodcontentstatements.add(ast_methodcontentstatement);
    }
    public ast_CatchPart getAst_catchpart() {
        return ast_catchpart;
    }

    public void setAst_catchpart(ast_CatchPart ast_catchpart) {
        this.ast_catchpart = ast_catchpart;
    }
    public ast_ConstructorStatement getAst_constructorstatement() {
        return ast_constructorstatement;
    }

    public void setAst_constructorstatement(ast_ConstructorStatement ast_constructorstatement) {
        this.ast_constructorstatement = ast_constructorstatement;
    }
    public ast_IfThenPart getAst_ifthenpart() {
        return ast_ifthenpart;
    }

    public void setAst_ifthenpart(ast_IfThenPart ast_ifthenpart) {
        this.ast_ifthenpart = ast_ifthenpart;
    }

}