





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_Constraint extends PackageableElement {






    private List<ClassesProv_Element> classesprov_elements;




    private ClassesProv_Namespace classesprov_namespace;




    private ClassesProv_Namespace classesprov_namespace;


    public ClassesProv_Constraint(
    ) {
        super(
        );
        this.classesprov_elements = new ArrayList<>();
    }

    public ClassesProv_Constraint(
        ArrayList<ClassesProv_Element> classesprov_elements    ) {
        this.classesprov_elements = classesprov_elements;
    }


    public List<ClassesProv_Element> getClassesprov_elements() {
        return classesprov_elements;
    }

    public void addClassesprov_element(Classesprov_element classesprov_element) {
        this.classesprov_elements.add(classesprov_element);
    }
    public ClassesProv_Namespace getClassesprov_namespace() {
        return classesprov_namespace;
    }

    public void setClassesprov_namespace(ClassesProv_Namespace classesprov_namespace) {
        this.classesprov_namespace = classesprov_namespace;
    }
    public ClassesProv_Namespace getClassesprov_namespace() {
        return classesprov_namespace;
    }

    public void setClassesprov_namespace(ClassesProv_Namespace classesprov_namespace) {
        this.classesprov_namespace = classesprov_namespace;
    }

}