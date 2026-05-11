





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_Relationship extends Element {






    private List<ClassesProv_Element> classesprov_elements;


    public ClassesProv_Relationship(
    ) {
        super(
        );
        this.classesprov_elements = new ArrayList<>();
    }

    public ClassesProv_Relationship(
        ArrayList<ClassesProv_Element> classesprov_elements    ) {
        this.classesprov_elements = classesprov_elements;
    }


    public List<ClassesProv_Element> getClassesprov_elements() {
        return classesprov_elements;
    }

    public void addClassesprov_element(Classesprov_element classesprov_element) {
        this.classesprov_elements.add(classesprov_element);
    }

}