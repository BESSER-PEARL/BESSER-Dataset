





import java.util.List;
import java.util.ArrayList;

public class Core_IType extends IMember {

    private String fullyQualifiedName;
    private String fullyQualifiedParametrizedName;





    private Core_IClassFile core_iclassfile;




    private Core_ICompilationUnit core_icompilationunit;




    private List<Core_ITypeParameter> core_itypeparameters;




    private Core_ICompilationUnit core_icompilationunit;




    private List<Core_IType> core_itypes;


    public Core_IType(
        String fullyQualifiedName,        String fullyQualifiedParametrizedName    ) {
        super(
        );
        this.fullyQualifiedName = fullyQualifiedName;
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.core_itypeparameters = new ArrayList<>();
        this.core_itypes = new ArrayList<>();
    }

    public Core_IType(
        String fullyQualifiedName,        String fullyQualifiedParametrizedName        ArrayList<Core_ITypeParameter> core_itypeparameters,        ArrayList<Core_IType> core_itypes    ) {
        this.fullyQualifiedName = fullyQualifiedName;
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.core_itypeparameters = core_itypeparameters;
        this.core_itypes = core_itypes;
    }

    public String getFullyqualifiedname() {
        return fullyQualifiedName;
    }

    public void setFullyqualifiedname(String fullyQualifiedName) {
        this.fullyQualifiedName = fullyQualifiedName;
    }
    public String getFullyqualifiedparametrizedname() {
        return fullyQualifiedParametrizedName;
    }

    public void setFullyqualifiedparametrizedname(String fullyQualifiedParametrizedName) {
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
    }

    public Core_IClassFile getCore_iclassfile() {
        return core_iclassfile;
    }

    public void setCore_iclassfile(Core_IClassFile core_iclassfile) {
        this.core_iclassfile = core_iclassfile;
    }
    public Core_ICompilationUnit getCore_icompilationunit() {
        return core_icompilationunit;
    }

    public void setCore_icompilationunit(Core_ICompilationUnit core_icompilationunit) {
        this.core_icompilationunit = core_icompilationunit;
    }
    public List<Core_ITypeParameter> getCore_itypeparameters() {
        return core_itypeparameters;
    }

    public void addCore_itypeparameter(Core_itypeparameter core_itypeparameter) {
        this.core_itypeparameters.add(core_itypeparameter);
    }
    public Core_ICompilationUnit getCore_icompilationunit() {
        return core_icompilationunit;
    }

    public void setCore_icompilationunit(Core_ICompilationUnit core_icompilationunit) {
        this.core_icompilationunit = core_icompilationunit;
    }
    public List<Core_IType> getCore_itypes() {
        return core_itypes;
    }

    public void addCore_itype(Core_itype core_itype) {
        this.core_itypes.add(core_itype);
    }

}