





import java.util.List;
import java.util.ArrayList;

public class frontend_patterns_PReference extends PFeature {






    private List<PObject> pobjects;


    public frontend_patterns_PReference(
    ) {
        super(
        );
        this.pobjects = new ArrayList<>();
    }

    public frontend_patterns_PReference(
        ArrayList<PObject> pobjects    ) {
        this.pobjects = pobjects;
    }


    public List<PObject> getPobjects() {
        return pobjects;
    }

    public void addPobject(Pobject pobject) {
        this.pobjects.add(pobject);
    }

}