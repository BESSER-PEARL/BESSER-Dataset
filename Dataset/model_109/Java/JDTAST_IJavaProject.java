





import java.util.List;
import java.util.ArrayList;

public class JDTAST_IJavaProject extends PhysicalElement, IJavaElement {






    private JDTAST_IJavaModel jdtast_ijavamodel;




    private List<JDTAST_IPackageFragmentRoot> jdtast_ipackagefragmentroots;




    private JDTAST_IJavaProject jdtast_ijavaproject;




    private List<JDTAST_IPackageFragmentRoot> jdtast_ipackagefragmentroots;


    public JDTAST_IJavaProject(
    ) {
        super(
        );
        this.jdtast_ipackagefragmentroots = new ArrayList<>();
        this.jdtast_ipackagefragmentroots = new ArrayList<>();
    }

    public JDTAST_IJavaProject(
        ArrayList<JDTAST_IPackageFragmentRoot> jdtast_ipackagefragmentroots,        ArrayList<JDTAST_IPackageFragmentRoot> jdtast_ipackagefragmentroots    ) {
        this.jdtast_ipackagefragmentroots = jdtast_ipackagefragmentroots;
        this.jdtast_ipackagefragmentroots = jdtast_ipackagefragmentroots;
    }


    public JDTAST_IJavaModel getJdtast_ijavamodel() {
        return jdtast_ijavamodel;
    }

    public void setJdtast_ijavamodel(JDTAST_IJavaModel jdtast_ijavamodel) {
        this.jdtast_ijavamodel = jdtast_ijavamodel;
    }
    public List<JDTAST_IPackageFragmentRoot> getJdtast_ipackagefragmentroots() {
        return jdtast_ipackagefragmentroots;
    }

    public void addJdtast_ipackagefragmentroot(Jdtast_ipackagefragmentroot jdtast_ipackagefragmentroot) {
        this.jdtast_ipackagefragmentroots.add(jdtast_ipackagefragmentroot);
    }
    public JDTAST_IJavaProject getJdtast_ijavaproject() {
        return jdtast_ijavaproject;
    }

    public void setJdtast_ijavaproject(JDTAST_IJavaProject jdtast_ijavaproject) {
        this.jdtast_ijavaproject = jdtast_ijavaproject;
    }
    public List<JDTAST_IPackageFragmentRoot> getJdtast_ipackagefragmentroots() {
        return jdtast_ipackagefragmentroots;
    }

    public void addJdtast_ipackagefragmentroot(Jdtast_ipackagefragmentroot jdtast_ipackagefragmentroot) {
        this.jdtast_ipackagefragmentroots.add(jdtast_ipackagefragmentroot);
    }

}