





import java.util.List;
import java.util.ArrayList;

public class altarica_Domain extends NamedElement {






    private List<altarica_NamedElement> altarica_namedelements;


    public altarica_Domain(
    ) {
        super(
        );
        this.altarica_namedelements = new ArrayList<>();
    }

    public altarica_Domain(
        ArrayList<altarica_NamedElement> altarica_namedelements    ) {
        this.altarica_namedelements = altarica_namedelements;
    }


    public List<altarica_NamedElement> getAltarica_namedelements() {
        return altarica_namedelements;
    }

    public void addAltarica_namedelement(Altarica_namedelement altarica_namedelement) {
        this.altarica_namedelements.add(altarica_namedelement);
    }

}