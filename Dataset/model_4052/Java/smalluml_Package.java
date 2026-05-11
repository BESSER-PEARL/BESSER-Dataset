





import java.util.List;
import java.util.ArrayList;

public class smalluml_Package extends NamedElement {






    private List<smalluml_NamedElement> smalluml_namedelements;


    public smalluml_Package(
    ) {
        super(
        );
        this.smalluml_namedelements = new ArrayList<>();
    }

    public smalluml_Package(
        ArrayList<smalluml_NamedElement> smalluml_namedelements    ) {
        this.smalluml_namedelements = smalluml_namedelements;
    }


    public List<smalluml_NamedElement> getSmalluml_namedelements() {
        return smalluml_namedelements;
    }

    public void addSmalluml_namedelement(Smalluml_namedelement smalluml_namedelement) {
        this.smalluml_namedelements.add(smalluml_namedelement);
    }

}