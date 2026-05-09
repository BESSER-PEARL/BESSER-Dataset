





import java.util.List;
import java.util.ArrayList;

public class JDTAST_IType extends IMember {

    private String fullyQualifiedName;
    private String fullyQualifiedParametrizedName;





    private JDTAST_IClassFile jdtast_iclassfile;




    private JDTAST_ICompilationUnit jdtast_icompilationunit;




    private JDTAST_ICompilationUnit jdtast_icompilationunit;




    private List<JDTAST_ITypeParameter> jdtast_itypeparameters;




    private List<JDTAST_IType> jdtast_itypes;


    public JDTAST_IType(
        String fullyQualifiedName,        String fullyQualifiedParametrizedName    ) {
        super(
        );
        this.fullyQualifiedName = fullyQualifiedName;
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.jdtast_itypeparameters = new ArrayList<>();
        this.jdtast_itypes = new ArrayList<>();
    }

    public JDTAST_IType(
        String fullyQualifiedName,        String fullyQualifiedParametrizedName        ArrayList<JDTAST_ITypeParameter> jdtast_itypeparameters,        ArrayList<JDTAST_IType> jdtast_itypes    ) {
        this.fullyQualifiedName = fullyQualifiedName;
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.jdtast_itypeparameters = jdtast_itypeparameters;
        this.jdtast_itypes = jdtast_itypes;
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

    public JDTAST_IClassFile getJdtast_iclassfile() {
        return jdtast_iclassfile;
    }

    public void setJdtast_iclassfile(JDTAST_IClassFile jdtast_iclassfile) {
        this.jdtast_iclassfile = jdtast_iclassfile;
    }
    public JDTAST_ICompilationUnit getJdtast_icompilationunit() {
        return jdtast_icompilationunit;
    }

    public void setJdtast_icompilationunit(JDTAST_ICompilationUnit jdtast_icompilationunit) {
        this.jdtast_icompilationunit = jdtast_icompilationunit;
    }
    public JDTAST_ICompilationUnit getJdtast_icompilationunit() {
        return jdtast_icompilationunit;
    }

    public void setJdtast_icompilationunit(JDTAST_ICompilationUnit jdtast_icompilationunit) {
        this.jdtast_icompilationunit = jdtast_icompilationunit;
    }
    public List<JDTAST_ITypeParameter> getJdtast_itypeparameters() {
        return jdtast_itypeparameters;
    }

    public void addJdtast_itypeparameter(Jdtast_itypeparameter jdtast_itypeparameter) {
        this.jdtast_itypeparameters.add(jdtast_itypeparameter);
    }
    public List<JDTAST_IType> getJdtast_itypes() {
        return jdtast_itypes;
    }

    public void addJdtast_itype(Jdtast_itype jdtast_itype) {
        this.jdtast_itypes.add(jdtast_itype);
    }

}