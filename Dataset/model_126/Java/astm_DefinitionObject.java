





import java.util.List;
import java.util.ArrayList;

public class astm_DefinitionObject extends GASTMSyntaxObject {






    private astm_CompilationUnit astm_compilationunit;




    private astm_DelphiWithStatement astm_delphiwithstatement;




    private astm_DelphiBlockStatement astm_delphiblockstatement;




    private astm_Scope astm_scope;


    public astm_DefinitionObject(
    ) {
        super(
        );
    }



    public astm_CompilationUnit getAstm_compilationunit() {
        return astm_compilationunit;
    }

    public void setAstm_compilationunit(astm_CompilationUnit astm_compilationunit) {
        this.astm_compilationunit = astm_compilationunit;
    }
    public astm_DelphiWithStatement getAstm_delphiwithstatement() {
        return astm_delphiwithstatement;
    }

    public void setAstm_delphiwithstatement(astm_DelphiWithStatement astm_delphiwithstatement) {
        this.astm_delphiwithstatement = astm_delphiwithstatement;
    }
    public astm_DelphiBlockStatement getAstm_delphiblockstatement() {
        return astm_delphiblockstatement;
    }

    public void setAstm_delphiblockstatement(astm_DelphiBlockStatement astm_delphiblockstatement) {
        this.astm_delphiblockstatement = astm_delphiblockstatement;
    }
    public astm_Scope getAstm_scope() {
        return astm_scope;
    }

    public void setAstm_scope(astm_Scope astm_scope) {
        this.astm_scope = astm_scope;
    }

}