





import java.util.List;
import java.util.ArrayList;

public class Core_ICompilationUnit extends ITypeRoot {






    private CompilationUnit compilationunit;




    private ICompilationUnit icompilationunit;


    public Core_ICompilationUnit(
    ) {
        super(
        );
    }



    public CompilationUnit getCompilationunit() {
        return compilationunit;
    }

    public void setCompilationunit(CompilationUnit compilationunit) {
        this.compilationunit = compilationunit;
    }
    public ICompilationUnit getIcompilationunit() {
        return icompilationunit;
    }

    public void setIcompilationunit(ICompilationUnit icompilationunit) {
        this.icompilationunit = icompilationunit;
    }

}