





import java.util.List;
import java.util.ArrayList;

public class spinefm_FMModel_FeatureModel  {

    private String name;
    private String id;





    private Feature feature;




    private List<Constraint> constraints;


    public spinefm_FMModel_FeatureModel(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
        this.constraints = new ArrayList<>();
    }

    public spinefm_FMModel_FeatureModel(
        String name,        String id        ArrayList<Constraint> constraints    ) {
        this.name = name;
        this.id = id;
        this.constraints = constraints;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Feature getFeature() {
        return feature;
    }

    public void setFeature(Feature feature) {
        this.feature = feature;
    }
    public List<Constraint> getConstraints() {
        return constraints;
    }

    public void addConstraint(Constraint constraint) {
        this.constraints.add(constraint);
    }

}