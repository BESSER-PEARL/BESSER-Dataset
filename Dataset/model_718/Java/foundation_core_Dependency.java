





import java.util.List;
import java.util.ArrayList;

public class foundation_core_Dependency extends Relationship {






    private List<ModelElement> modelelements;




    private List<ModelElement> modelelements;


    public foundation_core_Dependency(
    ) {
        super(
        );
        this.modelelements = new ArrayList<>();
        this.modelelements = new ArrayList<>();
    }

    public foundation_core_Dependency(
        ArrayList<ModelElement> modelelements,        ArrayList<ModelElement> modelelements    ) {
        this.modelelements = modelelements;
        this.modelelements = modelelements;
    }


    public List<ModelElement> getModelelements() {
        return modelelements;
    }

    public void addModelelement(Modelelement modelelement) {
        this.modelelements.add(modelelement);
    }
    public List<ModelElement> getModelelements() {
        return modelelements;
    }

    public void addModelelement(Modelelement modelelement) {
        this.modelelements.add(modelelement);
    }

}