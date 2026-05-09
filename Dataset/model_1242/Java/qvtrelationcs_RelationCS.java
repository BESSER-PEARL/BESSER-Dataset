





import java.util.List;
import java.util.ArrayList;

public class qvtrelationcs_RelationCS extends NamedElementCS {

    private boolean isTop;
    private boolean isDefault;





    private qvtrelationcs_PatternCS qvtrelationcs_patterncs;




    private qvtrelationcs_PatternCS qvtrelationcs_patterncs;




    private List<qvtrelationcs_VarDeclarationCS> qvtrelationcs_vardeclarationcss;




    private List<qvtrelationcs_AbstractDomainCS> qvtrelationcs_abstractdomaincss;


    public qvtrelationcs_RelationCS(
        boolean isTop,        boolean isDefault    ) {
        super(
        );
        this.isTop = isTop;
        this.isDefault = isDefault;
        this.qvtrelationcs_vardeclarationcss = new ArrayList<>();
        this.qvtrelationcs_abstractdomaincss = new ArrayList<>();
    }

    public qvtrelationcs_RelationCS(
        boolean isTop,        boolean isDefault        ArrayList<qvtrelationcs_VarDeclarationCS> qvtrelationcs_vardeclarationcss,        ArrayList<qvtrelationcs_AbstractDomainCS> qvtrelationcs_abstractdomaincss    ) {
        this.isTop = isTop;
        this.isDefault = isDefault;
        this.qvtrelationcs_vardeclarationcss = qvtrelationcs_vardeclarationcss;
        this.qvtrelationcs_abstractdomaincss = qvtrelationcs_abstractdomaincss;
    }

    public boolean getIstop() {
        return isTop;
    }

    public void setIstop(boolean isTop) {
        this.isTop = isTop;
    }
    public boolean getIsdefault() {
        return isDefault;
    }

    public void setIsdefault(boolean isDefault) {
        this.isDefault = isDefault;
    }

    public qvtrelationcs_PatternCS getQvtrelationcs_patterncs() {
        return qvtrelationcs_patterncs;
    }

    public void setQvtrelationcs_patterncs(qvtrelationcs_PatternCS qvtrelationcs_patterncs) {
        this.qvtrelationcs_patterncs = qvtrelationcs_patterncs;
    }
    public qvtrelationcs_PatternCS getQvtrelationcs_patterncs() {
        return qvtrelationcs_patterncs;
    }

    public void setQvtrelationcs_patterncs(qvtrelationcs_PatternCS qvtrelationcs_patterncs) {
        this.qvtrelationcs_patterncs = qvtrelationcs_patterncs;
    }
    public List<qvtrelationcs_VarDeclarationCS> getQvtrelationcs_vardeclarationcss() {
        return qvtrelationcs_vardeclarationcss;
    }

    public void addQvtrelationcs_vardeclarationcs(Qvtrelationcs_vardeclarationcs qvtrelationcs_vardeclarationcs) {
        this.qvtrelationcs_vardeclarationcss.add(qvtrelationcs_vardeclarationcs);
    }
    public List<qvtrelationcs_AbstractDomainCS> getQvtrelationcs_abstractdomaincss() {
        return qvtrelationcs_abstractdomaincss;
    }

    public void addQvtrelationcs_abstractdomaincs(Qvtrelationcs_abstractdomaincs qvtrelationcs_abstractdomaincs) {
        this.qvtrelationcs_abstractdomaincss.add(qvtrelationcs_abstractdomaincs);
    }

}