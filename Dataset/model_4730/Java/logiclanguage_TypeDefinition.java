





import java.util.List;
import java.util.ArrayList;

public class logiclanguage_TypeDefinition extends Type {






    private logiclanguage_DefinedElement logiclanguage_definedelement;




    private List<logiclanguage_DefinedElement> logiclanguage_definedelements;


    public logiclanguage_TypeDefinition(
    ) {
        super(
        );
        this.logiclanguage_definedelements = new ArrayList<>();
    }

    public logiclanguage_TypeDefinition(
        ArrayList<logiclanguage_DefinedElement> logiclanguage_definedelements    ) {
        this.logiclanguage_definedelements = logiclanguage_definedelements;
    }


    public logiclanguage_DefinedElement getLogiclanguage_definedelement() {
        return logiclanguage_definedelement;
    }

    public void setLogiclanguage_definedelement(logiclanguage_DefinedElement logiclanguage_definedelement) {
        this.logiclanguage_definedelement = logiclanguage_definedelement;
    }
    public List<logiclanguage_DefinedElement> getLogiclanguage_definedelements() {
        return logiclanguage_definedelements;
    }

    public void addLogiclanguage_definedelement(Logiclanguage_definedelement logiclanguage_definedelement) {
        this.logiclanguage_definedelements.add(logiclanguage_definedelement);
    }

}