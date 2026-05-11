





import java.util.List;
import java.util.ArrayList;

public class ClassM_StructuralFeature extends TypedElement {

    private String name;
    private String visibility;





    private ClassM_Class classm_class;




    private ClassM_Class classm_class;


    public ClassM_StructuralFeature(
        String name,        String visibility    ) {
        super(
        );
        this.name = name;
        this.visibility = visibility;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public ClassM_Class getClassm_class() {
        return classm_class;
    }

    public void setClassm_class(ClassM_Class classm_class) {
        this.classm_class = classm_class;
    }
    public ClassM_Class getClassm_class() {
        return classm_class;
    }

    public void setClassm_class(ClassM_Class classm_class) {
        this.classm_class = classm_class;
    }

}