





import java.util.List;
import java.util.ArrayList;

public class MARTE_Alloc_Allocate  {

    private String nature;
    private String kind;





    private List<NFPs_NfpConstraint> nfps_nfpconstraints;


    public MARTE_Alloc_Allocate(
        String nature,        String kind    ) {
        this.nature = nature;
        this.kind = kind;
        this.nfps_nfpconstraints = new ArrayList<>();
    }

    public MARTE_Alloc_Allocate(
        String nature,        String kind        ArrayList<NFPs_NfpConstraint> nfps_nfpconstraints    ) {
        this.nature = nature;
        this.kind = kind;
        this.nfps_nfpconstraints = nfps_nfpconstraints;
    }

    public String getNature() {
        return nature;
    }

    public void setNature(String nature) {
        this.nature = nature;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public List<NFPs_NfpConstraint> getNfps_nfpconstraints() {
        return nfps_nfpconstraints;
    }

    public void addNfps_nfpconstraint(Nfps_nfpconstraint nfps_nfpconstraint) {
        this.nfps_nfpconstraints.add(nfps_nfpconstraint);
    }

}