





import java.util.List;
import java.util.ArrayList;

public class emof_Tag extends Element {

    private String name;
    private String value;





    private emof_Element emof_element;




    private List<emof_Element> emof_elements;


    public emof_Tag(
        String name,        String value    ) {
        super(
        );
        this.name = name;
        this.value = value;
        this.emof_elements = new ArrayList<>();
    }

    public emof_Tag(
        String name,        String value        ArrayList<emof_Element> emof_elements    ) {
        this.name = name;
        this.value = value;
        this.emof_elements = emof_elements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public emof_Element getEmof_element() {
        return emof_element;
    }

    public void setEmof_element(emof_Element emof_element) {
        this.emof_element = emof_element;
    }
    public List<emof_Element> getEmof_elements() {
        return emof_elements;
    }

    public void addEmof_element(Emof_element emof_element) {
        this.emof_elements.add(emof_element);
    }

}