





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_DirectedRelationship extends Relationship {






    private List<ClassesProv_Element> classesprov_elements;




    private List<ClassesProv_Element> classesprov_elements;


    public ClassesProv_DirectedRelationship(
    ) {
        super(
        );
        this.classesprov_elements = new ArrayList<>();
        this.classesprov_elements = new ArrayList<>();
    }

    public ClassesProv_DirectedRelationship(
        ArrayList<ClassesProv_Element> classesprov_elements,        ArrayList<ClassesProv_Element> classesprov_elements    ) {
        this.classesprov_elements = classesprov_elements;
        this.classesprov_elements = classesprov_elements;
    }


    public List<ClassesProv_Element> getClassesprov_elements() {
        return classesprov_elements;
    }

    public void addClassesprov_element(Classesprov_element classesprov_element) {
        this.classesprov_elements.add(classesprov_element);
    }
    public List<ClassesProv_Element> getClassesprov_elements() {
        return classesprov_elements;
    }

    public void addClassesprov_element(Classesprov_element classesprov_element) {
        this.classesprov_elements.add(classesprov_element);
    }

}