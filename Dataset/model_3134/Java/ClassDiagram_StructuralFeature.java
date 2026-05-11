





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_StructuralFeature extends TypedElement {

    private String visibility;
    private String name;





    private ClassDiagram_Class classdiagram_class;




    private ClassDiagram_Class classdiagram_class;


    public ClassDiagram_StructuralFeature(
        String visibility,        String name    ) {
        super(
        );
        this.visibility = visibility;
        this.name = name;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ClassDiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(ClassDiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }
    public ClassDiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(ClassDiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }

}