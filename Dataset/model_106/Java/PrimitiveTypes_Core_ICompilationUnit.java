





import java.util.List;
import java.util.ArrayList;

public class PrimitiveTypes_Core_ICompilationUnit extends ITypeRoot {






    private CompilationUnit compilationunit;




    private List<Core_IType> core_itypes;




    private List<Core_IImportDeclaration> core_iimportdeclarations;




    private List<Core_IType> core_itypes;


    public PrimitiveTypes_Core_ICompilationUnit(
    ) {
        super(
        );
        this.core_itypes = new ArrayList<>();
        this.core_iimportdeclarations = new ArrayList<>();
        this.core_itypes = new ArrayList<>();
    }

    public PrimitiveTypes_Core_ICompilationUnit(
        ArrayList<Core_IType> core_itypes,        ArrayList<Core_IImportDeclaration> core_iimportdeclarations,        ArrayList<Core_IType> core_itypes    ) {
        this.core_itypes = core_itypes;
        this.core_iimportdeclarations = core_iimportdeclarations;
        this.core_itypes = core_itypes;
    }


    public CompilationUnit getCompilationunit() {
        return compilationunit;
    }

    public void setCompilationunit(CompilationUnit compilationunit) {
        this.compilationunit = compilationunit;
    }
    public List<Core_IType> getCore_itypes() {
        return core_itypes;
    }

    public void addCore_itype(Core_itype core_itype) {
        this.core_itypes.add(core_itype);
    }
    public List<Core_IImportDeclaration> getCore_iimportdeclarations() {
        return core_iimportdeclarations;
    }

    public void addCore_iimportdeclaration(Core_iimportdeclaration core_iimportdeclaration) {
        this.core_iimportdeclarations.add(core_iimportdeclaration);
    }
    public List<Core_IType> getCore_itypes() {
        return core_itypes;
    }

    public void addCore_itype(Core_itype core_itype) {
        this.core_itypes.add(core_itype);
    }

}