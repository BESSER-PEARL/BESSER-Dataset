





import java.util.List;
import java.util.ArrayList;

public class classmodel_Package extends Element {

    private String name;





    private List<classmodel_Element> classmodel_elements;


    public classmodel_Package(
        String name    ) {
        super(
        );
        this.name = name;
        this.classmodel_elements = new ArrayList<>();
    }

    public classmodel_Package(
        String name        ArrayList<classmodel_Element> classmodel_elements    ) {
        this.name = name;
        this.classmodel_elements = classmodel_elements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<classmodel_Element> getClassmodel_elements() {
        return classmodel_elements;
    }

    public void addClassmodel_element(Classmodel_element classmodel_element) {
        this.classmodel_elements.add(classmodel_element);
    }

}