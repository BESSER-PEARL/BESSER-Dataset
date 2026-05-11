





import java.util.List;
import java.util.ArrayList;

public class altarica_Variable extends NamedElement {






    private List<altarica_NamedElement> altarica_namedelements;




    private altarica_Type altarica_type;


    public altarica_Variable(
    ) {
        super(
        );
        this.altarica_namedelements = new ArrayList<>();
    }

    public altarica_Variable(
        ArrayList<altarica_NamedElement> altarica_namedelements    ) {
        this.altarica_namedelements = altarica_namedelements;
    }


    public List<altarica_NamedElement> getAltarica_namedelements() {
        return altarica_namedelements;
    }

    public void addAltarica_namedelement(Altarica_namedelement altarica_namedelement) {
        this.altarica_namedelements.add(altarica_namedelement);
    }
    public altarica_Type getAltarica_type() {
        return altarica_type;
    }

    public void setAltarica_type(altarica_Type altarica_type) {
        this.altarica_type = altarica_type;
    }

}