





import java.util.List;
import java.util.ArrayList;

public class JTLMM_emof_Comment extends Element {






    private List<NamedElement> namedelements;


    public JTLMM_emof_Comment(
    ) {
        super(
        );
        this.namedelements = new ArrayList<>();
    }

    public JTLMM_emof_Comment(
        ArrayList<NamedElement> namedelements    ) {
        this.namedelements = namedelements;
    }


    public List<NamedElement> getNamedelements() {
        return namedelements;
    }

    public void addNamedelement(Namedelement namedelement) {
        this.namedelements.add(namedelement);
    }

}