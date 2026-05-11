





import java.util.List;
import java.util.ArrayList;

public class gremlin_CustomStep extends Step {

    private String name;





    private List<gremlin_EObject> gremlin_eobjects;


    public gremlin_CustomStep(
        String name    ) {
        super(
        );
        this.name = name;
        this.gremlin_eobjects = new ArrayList<>();
    }

    public gremlin_CustomStep(
        String name        ArrayList<gremlin_EObject> gremlin_eobjects    ) {
        this.name = name;
        this.gremlin_eobjects = gremlin_eobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<gremlin_EObject> getGremlin_eobjects() {
        return gremlin_eobjects;
    }

    public void addGremlin_eobject(Gremlin_eobject gremlin_eobject) {
        this.gremlin_eobjects.add(gremlin_eobject);
    }

}