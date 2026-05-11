





import java.util.List;
import java.util.ArrayList;

public class jdtmm_JDTCompilationUnit extends JDTTypeRoot {






    private jdtmm_JDTPackageFragment jdtmm_jdtpackagefragment;




    private List<jdtmm_JDTType> jdtmm_jdttypes;




    private jdtmm_JDTType jdtmm_jdttype;




    private jdtmm_JDTPackageFragment jdtmm_jdtpackagefragment;


    public jdtmm_JDTCompilationUnit(
    ) {
        super(
        );
        this.jdtmm_jdttypes = new ArrayList<>();
    }

    public jdtmm_JDTCompilationUnit(
        ArrayList<jdtmm_JDTType> jdtmm_jdttypes    ) {
        this.jdtmm_jdttypes = jdtmm_jdttypes;
    }


    public jdtmm_JDTPackageFragment getJdtmm_jdtpackagefragment() {
        return jdtmm_jdtpackagefragment;
    }

    public void setJdtmm_jdtpackagefragment(jdtmm_JDTPackageFragment jdtmm_jdtpackagefragment) {
        this.jdtmm_jdtpackagefragment = jdtmm_jdtpackagefragment;
    }
    public List<jdtmm_JDTType> getJdtmm_jdttypes() {
        return jdtmm_jdttypes;
    }

    public void addJdtmm_jdttype(Jdtmm_jdttype jdtmm_jdttype) {
        this.jdtmm_jdttypes.add(jdtmm_jdttype);
    }
    public jdtmm_JDTType getJdtmm_jdttype() {
        return jdtmm_jdttype;
    }

    public void setJdtmm_jdttype(jdtmm_JDTType jdtmm_jdttype) {
        this.jdtmm_jdttype = jdtmm_jdttype;
    }
    public jdtmm_JDTPackageFragment getJdtmm_jdtpackagefragment() {
        return jdtmm_jdtpackagefragment;
    }

    public void setJdtmm_jdtpackagefragment(jdtmm_JDTPackageFragment jdtmm_jdtpackagefragment) {
        this.jdtmm_jdtpackagefragment = jdtmm_jdtpackagefragment;
    }

}