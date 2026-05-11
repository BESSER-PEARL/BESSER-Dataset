





import java.util.List;
import java.util.ArrayList;

public class simpleuml_UMLPackage  {






    private List<simpleuml_ModelElement> simpleuml_modelelements;


    public simpleuml_UMLPackage(
    ) {
        this.simpleuml_modelelements = new ArrayList<>();
    }

    public simpleuml_UMLPackage(
        ArrayList<simpleuml_ModelElement> simpleuml_modelelements    ) {
        this.simpleuml_modelelements = simpleuml_modelelements;
    }


    public List<simpleuml_ModelElement> getSimpleuml_modelelements() {
        return simpleuml_modelelements;
    }

    public void addSimpleuml_modelelement(Simpleuml_modelelement simpleuml_modelelement) {
        this.simpleuml_modelelements.add(simpleuml_modelelement);
    }

}