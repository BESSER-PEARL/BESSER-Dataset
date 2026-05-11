





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Operation extends StructuralFeature {






    private ClassDiagram_Parameter classdiagram_parameter;




    private List<ClassDiagram_Parameter> classdiagram_parameters;


    public ClassDiagram_Operation(
    ) {
        super(
        );
        this.classdiagram_parameters = new ArrayList<>();
    }

    public ClassDiagram_Operation(
        ArrayList<ClassDiagram_Parameter> classdiagram_parameters    ) {
        this.classdiagram_parameters = classdiagram_parameters;
    }


    public ClassDiagram_Parameter getClassdiagram_parameter() {
        return classdiagram_parameter;
    }

    public void setClassdiagram_parameter(ClassDiagram_Parameter classdiagram_parameter) {
        this.classdiagram_parameter = classdiagram_parameter;
    }
    public List<ClassDiagram_Parameter> getClassdiagram_parameters() {
        return classdiagram_parameters;
    }

    public void addClassdiagram_parameter(Classdiagram_parameter classdiagram_parameter) {
        this.classdiagram_parameters.add(classdiagram_parameter);
    }

}