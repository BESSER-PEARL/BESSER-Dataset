





import java.util.List;
import java.util.ArrayList;

public class Core_ICompilationUnit extends ITypeRoot {






    private ICompilationUnit icompilationunit;




    private CompilationUnit compilationunit;


    public Core_ICompilationUnit(
    ) {
        super(
        );
    }



    public ICompilationUnit getIcompilationunit() {
        return icompilationunit;
    }

    public void setIcompilationunit(ICompilationUnit icompilationunit) {
        this.icompilationunit = icompilationunit;
    }
    public CompilationUnit getCompilationunit() {
        return compilationunit;
    }

    public void setCompilationunit(CompilationUnit compilationunit) {
        this.compilationunit = compilationunit;
    }

}