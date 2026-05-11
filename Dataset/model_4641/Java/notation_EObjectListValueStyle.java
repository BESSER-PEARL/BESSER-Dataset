





import java.util.List;
import java.util.ArrayList;

public class notation_EObjectListValueStyle extends NamedStyle {






    private List<notation_EObject> notation_eobjects;


    public notation_EObjectListValueStyle(
    ) {
        super(
        );
        this.notation_eobjects = new ArrayList<>();
    }

    public notation_EObjectListValueStyle(
        ArrayList<notation_EObject> notation_eobjects    ) {
        this.notation_eobjects = notation_eobjects;
    }


    public List<notation_EObject> getNotation_eobjects() {
        return notation_eobjects;
    }

    public void addNotation_eobject(Notation_eobject notation_eobject) {
        this.notation_eobjects.add(notation_eobject);
    }

}