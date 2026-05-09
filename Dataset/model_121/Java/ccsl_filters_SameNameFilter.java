





import java.util.List;
import java.util.ArrayList;

public class ccsl_filters_SameNameFilter extends AtomicFilter {

    private String ignoreCase;





    private List<namedElements_NamedElement> namedelements_namedelements;


    public ccsl_filters_SameNameFilter(
        String ignoreCase    ) {
        super(
        );
        this.ignoreCase = ignoreCase;
        this.namedelements_namedelements = new ArrayList<>();
    }

    public ccsl_filters_SameNameFilter(
        String ignoreCase        ArrayList<namedElements_NamedElement> namedelements_namedelements    ) {
        this.ignoreCase = ignoreCase;
        this.namedelements_namedelements = namedelements_namedelements;
    }

    public String getIgnorecase() {
        return ignoreCase;
    }

    public void setIgnorecase(String ignoreCase) {
        this.ignoreCase = ignoreCase;
    }

    public List<namedElements_NamedElement> getNamedelements_namedelements() {
        return namedelements_namedelements;
    }

    public void addNamedelements_namedelement(Namedelements_namedelement namedelements_namedelement) {
        this.namedelements_namedelements.add(namedelements_namedelement);
    }

}