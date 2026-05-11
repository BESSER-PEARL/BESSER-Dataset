





import java.util.List;
import java.util.ArrayList;

public class Core_ICompilationUnit extends ITypeRoot {






    private Core_IPackageFragment core_ipackagefragment;




    private List<Core_IImportDeclaration> core_iimportdeclarations;




    private Core_ICompilationUnit core_icompilationunit;


    public Core_ICompilationUnit(
    ) {
        super(
        );
        this.core_iimportdeclarations = new ArrayList<>();
    }

    public Core_ICompilationUnit(
        ArrayList<Core_IImportDeclaration> core_iimportdeclarations    ) {
        this.core_iimportdeclarations = core_iimportdeclarations;
    }


    public Core_IPackageFragment getCore_ipackagefragment() {
        return core_ipackagefragment;
    }

    public void setCore_ipackagefragment(Core_IPackageFragment core_ipackagefragment) {
        this.core_ipackagefragment = core_ipackagefragment;
    }
    public List<Core_IImportDeclaration> getCore_iimportdeclarations() {
        return core_iimportdeclarations;
    }

    public void addCore_iimportdeclaration(Core_iimportdeclaration core_iimportdeclaration) {
        this.core_iimportdeclarations.add(core_iimportdeclaration);
    }
    public Core_ICompilationUnit getCore_icompilationunit() {
        return core_icompilationunit;
    }

    public void setCore_icompilationunit(Core_ICompilationUnit core_icompilationunit) {
        this.core_icompilationunit = core_icompilationunit;
    }

}