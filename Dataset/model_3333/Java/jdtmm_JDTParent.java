





import java.util.List;
import java.util.ArrayList;

public class jdtmm_JDTParent  {

    private String flags;





    private List<jdtmm_JDTJavaElement> jdtmm_jdtjavaelements;




    private jdtmm_JDTJavaElement jdtmm_jdtjavaelement;


    public jdtmm_JDTParent(
        String flags    ) {
        this.flags = flags;
        this.jdtmm_jdtjavaelements = new ArrayList<>();
    }

    public jdtmm_JDTParent(
        String flags        ArrayList<jdtmm_JDTJavaElement> jdtmm_jdtjavaelements    ) {
        this.flags = flags;
        this.jdtmm_jdtjavaelements = jdtmm_jdtjavaelements;
    }

    public String getFlags() {
        return flags;
    }

    public void setFlags(String flags) {
        this.flags = flags;
    }

    public List<jdtmm_JDTJavaElement> getJdtmm_jdtjavaelements() {
        return jdtmm_jdtjavaelements;
    }

    public void addJdtmm_jdtjavaelement(Jdtmm_jdtjavaelement jdtmm_jdtjavaelement) {
        this.jdtmm_jdtjavaelements.add(jdtmm_jdtjavaelement);
    }
    public jdtmm_JDTJavaElement getJdtmm_jdtjavaelement() {
        return jdtmm_jdtjavaelement;
    }

    public void setJdtmm_jdtjavaelement(jdtmm_JDTJavaElement jdtmm_jdtjavaelement) {
        this.jdtmm_jdtjavaelement = jdtmm_jdtjavaelement;
    }

}