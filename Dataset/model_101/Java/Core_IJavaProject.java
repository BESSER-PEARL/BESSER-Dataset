





import java.util.List;
import java.util.ArrayList;

public class Core_IJavaProject extends IJavaElement, PhysicalElement {






    private List<IJavaProject> ijavaprojects;




    private List<IPackageFragmentRoot> ipackagefragmentroots;




    private List<IPackageFragmentRoot> ipackagefragmentroots;


    public Core_IJavaProject(
    ) {
        super(
        );
        this.ijavaprojects = new ArrayList<>();
        this.ipackagefragmentroots = new ArrayList<>();
        this.ipackagefragmentroots = new ArrayList<>();
    }

    public Core_IJavaProject(
        ArrayList<IJavaProject> ijavaprojects,        ArrayList<IPackageFragmentRoot> ipackagefragmentroots,        ArrayList<IPackageFragmentRoot> ipackagefragmentroots    ) {
        this.ijavaprojects = ijavaprojects;
        this.ipackagefragmentroots = ipackagefragmentroots;
        this.ipackagefragmentroots = ipackagefragmentroots;
    }


    public List<IJavaProject> getIjavaprojects() {
        return ijavaprojects;
    }

    public void addIjavaproject(Ijavaproject ijavaproject) {
        this.ijavaprojects.add(ijavaproject);
    }
    public List<IPackageFragmentRoot> getIpackagefragmentroots() {
        return ipackagefragmentroots;
    }

    public void addIpackagefragmentroot(Ipackagefragmentroot ipackagefragmentroot) {
        this.ipackagefragmentroots.add(ipackagefragmentroot);
    }
    public List<IPackageFragmentRoot> getIpackagefragmentroots() {
        return ipackagefragmentroots;
    }

    public void addIpackagefragmentroot(Ipackagefragmentroot ipackagefragmentroot) {
        this.ipackagefragmentroots.add(ipackagefragmentroot);
    }

}