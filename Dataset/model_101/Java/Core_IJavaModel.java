





import java.util.List;
import java.util.ArrayList;

public class Core_IJavaModel extends PhysicalElement {






    private List<IJavaProject> ijavaprojects;




    private List<IPackageFragmentRoot> ipackagefragmentroots;


    public Core_IJavaModel(
    ) {
        super(
        );
        this.ijavaprojects = new ArrayList<>();
        this.ipackagefragmentroots = new ArrayList<>();
    }

    public Core_IJavaModel(
        ArrayList<IJavaProject> ijavaprojects,        ArrayList<IPackageFragmentRoot> ipackagefragmentroots    ) {
        this.ijavaprojects = ijavaprojects;
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

}