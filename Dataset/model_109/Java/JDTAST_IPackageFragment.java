





import java.util.List;
import java.util.ArrayList;

public class JDTAST_IPackageFragment extends PhysicalElement, IJavaElement {

    private String isDefaultPackage;





    private JDTAST_IPackageFragmentRoot jdtast_ipackagefragmentroot;




    private List<JDTAST_IClassFile> jdtast_iclassfiles;




    private JDTAST_IPackageFragmentRoot jdtast_ipackagefragmentroot;




    private List<JDTAST_ICompilationUnit> jdtast_icompilationunits;


    public JDTAST_IPackageFragment(
        String isDefaultPackage    ) {
        super(
        );
        this.isDefaultPackage = isDefaultPackage;
        this.jdtast_iclassfiles = new ArrayList<>();
        this.jdtast_icompilationunits = new ArrayList<>();
    }

    public JDTAST_IPackageFragment(
        String isDefaultPackage        ArrayList<JDTAST_IClassFile> jdtast_iclassfiles,        ArrayList<JDTAST_ICompilationUnit> jdtast_icompilationunits    ) {
        this.isDefaultPackage = isDefaultPackage;
        this.jdtast_iclassfiles = jdtast_iclassfiles;
        this.jdtast_icompilationunits = jdtast_icompilationunits;
    }

    public String getIsdefaultpackage() {
        return isDefaultPackage;
    }

    public void setIsdefaultpackage(String isDefaultPackage) {
        this.isDefaultPackage = isDefaultPackage;
    }

    public JDTAST_IPackageFragmentRoot getJdtast_ipackagefragmentroot() {
        return jdtast_ipackagefragmentroot;
    }

    public void setJdtast_ipackagefragmentroot(JDTAST_IPackageFragmentRoot jdtast_ipackagefragmentroot) {
        this.jdtast_ipackagefragmentroot = jdtast_ipackagefragmentroot;
    }
    public List<JDTAST_IClassFile> getJdtast_iclassfiles() {
        return jdtast_iclassfiles;
    }

    public void addJdtast_iclassfile(Jdtast_iclassfile jdtast_iclassfile) {
        this.jdtast_iclassfiles.add(jdtast_iclassfile);
    }
    public JDTAST_IPackageFragmentRoot getJdtast_ipackagefragmentroot() {
        return jdtast_ipackagefragmentroot;
    }

    public void setJdtast_ipackagefragmentroot(JDTAST_IPackageFragmentRoot jdtast_ipackagefragmentroot) {
        this.jdtast_ipackagefragmentroot = jdtast_ipackagefragmentroot;
    }
    public List<JDTAST_ICompilationUnit> getJdtast_icompilationunits() {
        return jdtast_icompilationunits;
    }

    public void addJdtast_icompilationunit(Jdtast_icompilationunit jdtast_icompilationunit) {
        this.jdtast_icompilationunits.add(jdtast_icompilationunit);
    }

}