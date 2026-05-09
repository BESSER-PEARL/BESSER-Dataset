





import java.util.List;
import java.util.ArrayList;

public class astm_DefinitionObject extends GASTMSyntaxObject {






    private astm_CompilationUnit astm_compilationunit;




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
    public astm_Scope getAstm_scope() {
        return astm_scope;
    }

    public void setAstm_scope(astm_Scope astm_scope) {
        this.astm_scope = astm_scope;
    }

}