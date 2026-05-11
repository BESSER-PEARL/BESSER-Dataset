





import java.util.List;
import java.util.ArrayList;

public class classes_BehavioralFeature extends Feature {

    private boolean abstract;





    private List<classes_Parameter> classes_parameters;


    public classes_BehavioralFeature(
        boolean abstract    ) {
        super(
        );
        this.abstract = abstract;
        this.classes_parameters = new ArrayList<>();
    }

    public classes_BehavioralFeature(
        boolean abstract        ArrayList<classes_Parameter> classes_parameters    ) {
        this.abstract = abstract;
        this.classes_parameters = classes_parameters;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public List<classes_Parameter> getClasses_parameters() {
        return classes_parameters;
    }

    public void addClasses_parameter(Classes_parameter classes_parameter) {
        this.classes_parameters.add(classes_parameter);
    }

}