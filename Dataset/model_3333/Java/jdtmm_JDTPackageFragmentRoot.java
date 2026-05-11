





import java.util.List;
import java.util.ArrayList;

public class jdtmm_JDTPackageFragmentRoot extends JDTParentJavaElement {






    private jdtmm_JDTJavaProject jdtmm_jdtjavaproject;




    private List<jdtmm_JDTPackageFragment> jdtmm_jdtpackagefragments;




    private jdtmm_JDTPackageFragment jdtmm_jdtpackagefragment;




    private jdtmm_JDTJavaProject jdtmm_jdtjavaproject;


    public jdtmm_JDTPackageFragmentRoot(
    ) {
        super(
        );
        this.jdtmm_jdtpackagefragments = new ArrayList<>();
    }

    public jdtmm_JDTPackageFragmentRoot(
        ArrayList<jdtmm_JDTPackageFragment> jdtmm_jdtpackagefragments    ) {
        this.jdtmm_jdtpackagefragments = jdtmm_jdtpackagefragments;
    }


    public jdtmm_JDTJavaProject getJdtmm_jdtjavaproject() {
        return jdtmm_jdtjavaproject;
    }

    public void setJdtmm_jdtjavaproject(jdtmm_JDTJavaProject jdtmm_jdtjavaproject) {
        this.jdtmm_jdtjavaproject = jdtmm_jdtjavaproject;
    }
    public List<jdtmm_JDTPackageFragment> getJdtmm_jdtpackagefragments() {
        return jdtmm_jdtpackagefragments;
    }

    public void addJdtmm_jdtpackagefragment(Jdtmm_jdtpackagefragment jdtmm_jdtpackagefragment) {
        this.jdtmm_jdtpackagefragments.add(jdtmm_jdtpackagefragment);
    }
    public jdtmm_JDTPackageFragment getJdtmm_jdtpackagefragment() {
        return jdtmm_jdtpackagefragment;
    }

    public void setJdtmm_jdtpackagefragment(jdtmm_JDTPackageFragment jdtmm_jdtpackagefragment) {
        this.jdtmm_jdtpackagefragment = jdtmm_jdtpackagefragment;
    }
    public jdtmm_JDTJavaProject getJdtmm_jdtjavaproject() {
        return jdtmm_jdtjavaproject;
    }

    public void setJdtmm_jdtjavaproject(jdtmm_JDTJavaProject jdtmm_jdtjavaproject) {
        this.jdtmm_jdtjavaproject = jdtmm_jdtjavaproject;
    }

}