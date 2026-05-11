





import java.util.List;
import java.util.ArrayList;

public class jdtmm_JDTJavaModel extends JDTParentJavaElement {






    private jdtmm_JDTJavaProject jdtmm_jdtjavaproject;




    private List<jdtmm_JDTJavaProject> jdtmm_jdtjavaprojects;


    public jdtmm_JDTJavaModel(
    ) {
        super(
        );
        this.jdtmm_jdtjavaprojects = new ArrayList<>();
    }

    public jdtmm_JDTJavaModel(
        ArrayList<jdtmm_JDTJavaProject> jdtmm_jdtjavaprojects    ) {
        this.jdtmm_jdtjavaprojects = jdtmm_jdtjavaprojects;
    }


    public jdtmm_JDTJavaProject getJdtmm_jdtjavaproject() {
        return jdtmm_jdtjavaproject;
    }

    public void setJdtmm_jdtjavaproject(jdtmm_JDTJavaProject jdtmm_jdtjavaproject) {
        this.jdtmm_jdtjavaproject = jdtmm_jdtjavaproject;
    }
    public List<jdtmm_JDTJavaProject> getJdtmm_jdtjavaprojects() {
        return jdtmm_jdtjavaprojects;
    }

    public void addJdtmm_jdtjavaproject(Jdtmm_jdtjavaproject jdtmm_jdtjavaproject) {
        this.jdtmm_jdtjavaprojects.add(jdtmm_jdtjavaproject);
    }

}