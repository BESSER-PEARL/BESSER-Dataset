





import java.util.List;
import java.util.ArrayList;

public class foundation_core_PresentationElement extends Element {






    private List<ModelElement> modelelements;


    public foundation_core_PresentationElement(
    ) {
        super(
        );
        this.modelelements = new ArrayList<>();
    }

    public foundation_core_PresentationElement(
        ArrayList<ModelElement> modelelements    ) {
        this.modelelements = modelelements;
    }


    public List<ModelElement> getModelelements() {
        return modelelements;
    }

    public void addModelelement(Modelelement modelelement) {
        this.modelelements.add(modelelement);
    }

}