





import java.util.List;
import java.util.ArrayList;

public class behavior_RedefinableElement extends NamedElement {






    private List<behavior_RedefinableElement> behavior_redefinableelements;


    public behavior_RedefinableElement(
    ) {
        super(
        );
        this.behavior_redefinableelements = new ArrayList<>();
    }

    public behavior_RedefinableElement(
        ArrayList<behavior_RedefinableElement> behavior_redefinableelements    ) {
        this.behavior_redefinableelements = behavior_redefinableelements;
    }


    public List<behavior_RedefinableElement> getBehavior_redefinableelements() {
        return behavior_redefinableelements;
    }

    public void addBehavior_redefinableelement(Behavior_redefinableelement behavior_redefinableelement) {
        this.behavior_redefinableelements.add(behavior_redefinableelement);
    }

}