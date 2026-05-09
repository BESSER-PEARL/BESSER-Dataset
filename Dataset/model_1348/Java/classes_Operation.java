





import java.util.List;
import java.util.ArrayList;

public class classes_Operation extends TypedElement, NamedElement {






    private List<classes_Parameter> classes_parameters;


    public classes_Operation(
    ) {
        super(
        );
        this.classes_parameters = new ArrayList<>();
    }

    public classes_Operation(
        ArrayList<classes_Parameter> classes_parameters    ) {
        this.classes_parameters = classes_parameters;
    }


    public List<classes_Parameter> getClasses_parameters() {
        return classes_parameters;
    }

    public void addClasses_parameter(Classes_parameter classes_parameter) {
        this.classes_parameters.add(classes_parameter);
    }

}