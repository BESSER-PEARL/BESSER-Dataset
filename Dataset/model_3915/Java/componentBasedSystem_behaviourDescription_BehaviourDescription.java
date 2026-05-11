





import java.util.List;
import java.util.ArrayList;

public class componentBasedSystem_behaviourDescription_BehaviourDescription  {






    private List<DescriptionElement> descriptionelements;


    public componentBasedSystem_behaviourDescription_BehaviourDescription(
    ) {
        this.descriptionelements = new ArrayList<>();
    }

    public componentBasedSystem_behaviourDescription_BehaviourDescription(
        ArrayList<DescriptionElement> descriptionelements    ) {
        this.descriptionelements = descriptionelements;
    }


    public List<DescriptionElement> getDescriptionelements() {
        return descriptionelements;
    }

    public void addDescriptionelement(Descriptionelement descriptionelement) {
        this.descriptionelements.add(descriptionelement);
    }

}