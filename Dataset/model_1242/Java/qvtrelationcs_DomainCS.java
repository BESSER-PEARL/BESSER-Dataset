





import java.util.List;
import java.util.ArrayList;

public class qvtrelationcs_DomainCS extends AbstractDomainCS {

    private boolean isEnforce;
    private boolean isCheckonly;
    private String implementedBy;
    private boolean isReplace;





    private List<qvtrelationcs_DomainPatternCS> qvtrelationcs_domainpatterncss;




    private List<qvtrelationcs_DefaultValueCS> qvtrelationcs_defaultvaluecss;




    private qvtrelationcs_ExpCS qvtrelationcs_expcs;




    private qvtrelationcs_TypedModel qvtrelationcs_typedmodel;


    public qvtrelationcs_DomainCS(
        boolean isEnforce,        boolean isCheckonly,        String implementedBy,        boolean isReplace    ) {
        super(
        );
        this.isEnforce = isEnforce;
        this.isCheckonly = isCheckonly;
        this.implementedBy = implementedBy;
        this.isReplace = isReplace;
        this.qvtrelationcs_domainpatterncss = new ArrayList<>();
        this.qvtrelationcs_defaultvaluecss = new ArrayList<>();
    }

    public qvtrelationcs_DomainCS(
        boolean isEnforce,        boolean isCheckonly,        String implementedBy,        boolean isReplace        ArrayList<qvtrelationcs_DomainPatternCS> qvtrelationcs_domainpatterncss,        ArrayList<qvtrelationcs_DefaultValueCS> qvtrelationcs_defaultvaluecss    ) {
        this.isEnforce = isEnforce;
        this.isCheckonly = isCheckonly;
        this.implementedBy = implementedBy;
        this.isReplace = isReplace;
        this.qvtrelationcs_domainpatterncss = qvtrelationcs_domainpatterncss;
        this.qvtrelationcs_defaultvaluecss = qvtrelationcs_defaultvaluecss;
    }

    public boolean getIsenforce() {
        return isEnforce;
    }

    public void setIsenforce(boolean isEnforce) {
        this.isEnforce = isEnforce;
    }
    public boolean getIscheckonly() {
        return isCheckonly;
    }

    public void setIscheckonly(boolean isCheckonly) {
        this.isCheckonly = isCheckonly;
    }
    public String getImplementedby() {
        return implementedBy;
    }

    public void setImplementedby(String implementedBy) {
        this.implementedBy = implementedBy;
    }
    public boolean getIsreplace() {
        return isReplace;
    }

    public void setIsreplace(boolean isReplace) {
        this.isReplace = isReplace;
    }

    public List<qvtrelationcs_DomainPatternCS> getQvtrelationcs_domainpatterncss() {
        return qvtrelationcs_domainpatterncss;
    }

    public void addQvtrelationcs_domainpatterncs(Qvtrelationcs_domainpatterncs qvtrelationcs_domainpatterncs) {
        this.qvtrelationcs_domainpatterncss.add(qvtrelationcs_domainpatterncs);
    }
    public List<qvtrelationcs_DefaultValueCS> getQvtrelationcs_defaultvaluecss() {
        return qvtrelationcs_defaultvaluecss;
    }

    public void addQvtrelationcs_defaultvaluecs(Qvtrelationcs_defaultvaluecs qvtrelationcs_defaultvaluecs) {
        this.qvtrelationcs_defaultvaluecss.add(qvtrelationcs_defaultvaluecs);
    }
    public qvtrelationcs_ExpCS getQvtrelationcs_expcs() {
        return qvtrelationcs_expcs;
    }

    public void setQvtrelationcs_expcs(qvtrelationcs_ExpCS qvtrelationcs_expcs) {
        this.qvtrelationcs_expcs = qvtrelationcs_expcs;
    }
    public qvtrelationcs_TypedModel getQvtrelationcs_typedmodel() {
        return qvtrelationcs_typedmodel;
    }

    public void setQvtrelationcs_typedmodel(qvtrelationcs_TypedModel qvtrelationcs_typedmodel) {
        this.qvtrelationcs_typedmodel = qvtrelationcs_typedmodel;
    }

}