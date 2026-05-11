





import java.util.List;
import java.util.ArrayList;

public class siple_ProcedureDeclaration extends Declaration {

    private String ReturnType;





    private siple_CompilationUnit siple_compilationunit;


    public siple_ProcedureDeclaration(
        String ReturnType    ) {
        super(
        );
        this.ReturnType = ReturnType;
    }


    public String getReturntype() {
        return ReturnType;
    }

    public void setReturntype(String ReturnType) {
        this.ReturnType = ReturnType;
    }

    public siple_CompilationUnit getSiple_compilationunit() {
        return siple_compilationunit;
    }

    public void setSiple_compilationunit(siple_CompilationUnit siple_compilationunit) {
        this.siple_compilationunit = siple_compilationunit;
    }

}