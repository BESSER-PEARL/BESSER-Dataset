





import java.util.List;
import java.util.ArrayList;

public class Core_ICompilationUnit extends ITypeRoot {






    private ICompilationUnit icompilationunit;




    private PrimitiveTypes_Core_ICompilationUnit primitivetypes_core_icompilationunit;




    private PrimitiveTypes_Core_IPackageFragment primitivetypes_core_ipackagefragment;




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
    public PrimitiveTypes_Core_ICompilationUnit getPrimitivetypes_core_icompilationunit() {
        return primitivetypes_core_icompilationunit;
    }

    public void setPrimitivetypes_core_icompilationunit(PrimitiveTypes_Core_ICompilationUnit primitivetypes_core_icompilationunit) {
        this.primitivetypes_core_icompilationunit = primitivetypes_core_icompilationunit;
    }
    public PrimitiveTypes_Core_IPackageFragment getPrimitivetypes_core_ipackagefragment() {
        return primitivetypes_core_ipackagefragment;
    }

    public void setPrimitivetypes_core_ipackagefragment(PrimitiveTypes_Core_IPackageFragment primitivetypes_core_ipackagefragment) {
        this.primitivetypes_core_ipackagefragment = primitivetypes_core_ipackagefragment;
    }
    public CompilationUnit getCompilationunit() {
        return compilationunit;
    }

    public void setCompilationunit(CompilationUnit compilationunit) {
        this.compilationunit = compilationunit;
    }

}