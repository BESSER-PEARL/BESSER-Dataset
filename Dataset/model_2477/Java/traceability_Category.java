





import java.util.List;
import java.util.ArrayList;

public class traceability_Category  {

    private String name;





    private List<traceability_EObject> traceability_eobjects;


    public traceability_Category(
        String name    ) {
        this.name = name;
        this.traceability_eobjects = new ArrayList<>();
    }

    public traceability_Category(
        String name        ArrayList<traceability_EObject> traceability_eobjects    ) {
        this.name = name;
        this.traceability_eobjects = traceability_eobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<traceability_EObject> getTraceability_eobjects() {
        return traceability_eobjects;
    }

    public void addTraceability_eobject(Traceability_eobject traceability_eobject) {
        this.traceability_eobjects.add(traceability_eobject);
    }

}