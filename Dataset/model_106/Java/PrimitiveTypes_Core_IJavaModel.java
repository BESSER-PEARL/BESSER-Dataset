





import java.util.List;
import java.util.ArrayList;

public class PrimitiveTypes_Core_IJavaModel extends PhysicalElement {






    private List<Core_IPackageFragmentRoot> core_ipackagefragmentroots;




    private List<Core_IJavaProject> core_ijavaprojects;


    public PrimitiveTypes_Core_IJavaModel(
    ) {
        super(
        );
        this.core_ipackagefragmentroots = new ArrayList<>();
        this.core_ijavaprojects = new ArrayList<>();
    }

    public PrimitiveTypes_Core_IJavaModel(
        ArrayList<Core_IPackageFragmentRoot> core_ipackagefragmentroots,        ArrayList<Core_IJavaProject> core_ijavaprojects    ) {
        this.core_ipackagefragmentroots = core_ipackagefragmentroots;
        this.core_ijavaprojects = core_ijavaprojects;
    }


    public List<Core_IPackageFragmentRoot> getCore_ipackagefragmentroots() {
        return core_ipackagefragmentroots;
    }

    public void addCore_ipackagefragmentroot(Core_ipackagefragmentroot core_ipackagefragmentroot) {
        this.core_ipackagefragmentroots.add(core_ipackagefragmentroot);
    }
    public List<Core_IJavaProject> getCore_ijavaprojects() {
        return core_ijavaprojects;
    }

    public void addCore_ijavaproject(Core_ijavaproject core_ijavaproject) {
        this.core_ijavaprojects.add(core_ijavaproject);
    }

}