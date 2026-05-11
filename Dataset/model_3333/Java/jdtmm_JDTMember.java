





import java.util.List;
import java.util.ArrayList;

public class jdtmm_JDTMember extends JDTParentJavaElement {

    private String explicitPlainTextRequiredImports;
    private String visibility;





    private List<jdtmm_JDTType> jdtmm_jdttypes;


    public jdtmm_JDTMember(
        String explicitPlainTextRequiredImports,        String visibility    ) {
        super(
        );
        this.explicitPlainTextRequiredImports = explicitPlainTextRequiredImports;
        this.visibility = visibility;
        this.jdtmm_jdttypes = new ArrayList<>();
    }

    public jdtmm_JDTMember(
        String explicitPlainTextRequiredImports,        String visibility        ArrayList<jdtmm_JDTType> jdtmm_jdttypes    ) {
        this.explicitPlainTextRequiredImports = explicitPlainTextRequiredImports;
        this.visibility = visibility;
        this.jdtmm_jdttypes = jdtmm_jdttypes;
    }

    public String getExplicitplaintextrequiredimports() {
        return explicitPlainTextRequiredImports;
    }

    public void setExplicitplaintextrequiredimports(String explicitPlainTextRequiredImports) {
        this.explicitPlainTextRequiredImports = explicitPlainTextRequiredImports;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public List<jdtmm_JDTType> getJdtmm_jdttypes() {
        return jdtmm_jdttypes;
    }

    public void addJdtmm_jdttype(Jdtmm_jdttype jdtmm_jdttype) {
        this.jdtmm_jdttypes.add(jdtmm_jdttype);
    }

}