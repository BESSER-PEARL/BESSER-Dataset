





import java.util.List;
import java.util.ArrayList;

public class MARTE_Alloc_Assign  {

    private String kind;
    private String nature;





    private List<NFPs_NfpConstraint> nfps_nfpconstraints;


    public MARTE_Alloc_Assign(
        String kind,        String nature    ) {
        this.kind = kind;
        this.nature = nature;
        this.nfps_nfpconstraints = new ArrayList<>();
    }

    public MARTE_Alloc_Assign(
        String kind,        String nature        ArrayList<NFPs_NfpConstraint> nfps_nfpconstraints    ) {
        this.kind = kind;
        this.nature = nature;
        this.nfps_nfpconstraints = nfps_nfpconstraints;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getNature() {
        return nature;
    }

    public void setNature(String nature) {
        this.nature = nature;
    }

    public List<NFPs_NfpConstraint> getNfps_nfpconstraints() {
        return nfps_nfpconstraints;
    }

    public void addNfps_nfpconstraint(Nfps_nfpconstraint nfps_nfpconstraint) {
        this.nfps_nfpconstraints.add(nfps_nfpconstraint);
    }

}