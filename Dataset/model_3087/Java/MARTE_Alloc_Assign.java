





import java.util.List;
import java.util.ArrayList;

public class MARTE_Alloc_Assign  {






    private List<Alloc_MARTE_Element> alloc_marte_elements;




    private List<Alloc_MARTE_Element> alloc_marte_elements;




    private List<NFPs_NfpConstraint> nfps_nfpconstraints;




    private Alloc_MARTE_Comment alloc_marte_comment;


    public MARTE_Alloc_Assign(
    ) {
        this.alloc_marte_elements = new ArrayList<>();
        this.alloc_marte_elements = new ArrayList<>();
        this.nfps_nfpconstraints = new ArrayList<>();
    }

    public MARTE_Alloc_Assign(
        ArrayList<Alloc_MARTE_Element> alloc_marte_elements,        ArrayList<Alloc_MARTE_Element> alloc_marte_elements,        ArrayList<NFPs_NfpConstraint> nfps_nfpconstraints    ) {
        this.alloc_marte_elements = alloc_marte_elements;
        this.alloc_marte_elements = alloc_marte_elements;
        this.nfps_nfpconstraints = nfps_nfpconstraints;
    }


    public List<Alloc_MARTE_Element> getAlloc_marte_elements() {
        return alloc_marte_elements;
    }

    public void addAlloc_marte_element(Alloc_marte_element alloc_marte_element) {
        this.alloc_marte_elements.add(alloc_marte_element);
    }
    public List<Alloc_MARTE_Element> getAlloc_marte_elements() {
        return alloc_marte_elements;
    }

    public void addAlloc_marte_element(Alloc_marte_element alloc_marte_element) {
        this.alloc_marte_elements.add(alloc_marte_element);
    }
    public List<NFPs_NfpConstraint> getNfps_nfpconstraints() {
        return nfps_nfpconstraints;
    }

    public void addNfps_nfpconstraint(Nfps_nfpconstraint nfps_nfpconstraint) {
        this.nfps_nfpconstraints.add(nfps_nfpconstraint);
    }
    public Alloc_MARTE_Comment getAlloc_marte_comment() {
        return alloc_marte_comment;
    }

    public void setAlloc_marte_comment(Alloc_MARTE_Comment alloc_marte_comment) {
        this.alloc_marte_comment = alloc_marte_comment;
    }

}