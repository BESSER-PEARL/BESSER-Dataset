





import java.util.List;
import java.util.ArrayList;

public class Core_IPackageFragment extends IJavaElement, PhysicalElement {

    private String isDefaultPackage;





    private List<ICompilationUnit> icompilationunits;




    private List<IClassFile> iclassfiles;


    public Core_IPackageFragment(
        String isDefaultPackage    ) {
        super(
        );
        this.isDefaultPackage = isDefaultPackage;
        this.icompilationunits = new ArrayList<>();
        this.iclassfiles = new ArrayList<>();
    }

    public Core_IPackageFragment(
        String isDefaultPackage        ArrayList<ICompilationUnit> icompilationunits,        ArrayList<IClassFile> iclassfiles    ) {
        this.isDefaultPackage = isDefaultPackage;
        this.icompilationunits = icompilationunits;
        this.iclassfiles = iclassfiles;
    }

    public String getIsdefaultpackage() {
        return isDefaultPackage;
    }

    public void setIsdefaultpackage(String isDefaultPackage) {
        this.isDefaultPackage = isDefaultPackage;
    }

    public List<ICompilationUnit> getIcompilationunits() {
        return icompilationunits;
    }

    public void addIcompilationunit(Icompilationunit icompilationunit) {
        this.icompilationunits.add(icompilationunit);
    }
    public List<IClassFile> getIclassfiles() {
        return iclassfiles;
    }

    public void addIclassfile(Iclassfile iclassfile) {
        this.iclassfiles.add(iclassfile);
    }

}