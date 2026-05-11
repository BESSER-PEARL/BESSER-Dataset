





import java.util.List;
import java.util.ArrayList;

public class ClassM_Operation extends StructuralFeature {






    private ClassM_Parameter classm_parameter;




    private List<ClassM_Parameter> classm_parameters;


    public ClassM_Operation(
    ) {
        super(
        );
        this.classm_parameters = new ArrayList<>();
    }

    public ClassM_Operation(
        ArrayList<ClassM_Parameter> classm_parameters    ) {
        this.classm_parameters = classm_parameters;
    }


    public ClassM_Parameter getClassm_parameter() {
        return classm_parameter;
    }

    public void setClassm_parameter(ClassM_Parameter classm_parameter) {
        this.classm_parameter = classm_parameter;
    }
    public List<ClassM_Parameter> getClassm_parameters() {
        return classm_parameters;
    }

    public void addClassm_parameter(Classm_parameter classm_parameter) {
        this.classm_parameters.add(classm_parameter);
    }

}