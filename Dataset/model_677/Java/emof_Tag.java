





import java.util.List;
import java.util.ArrayList;

public class emof_Tag extends Element {

    private String value;
    private String name;





    private emof_Element emof_element;




    private List<emof_Element> emof_elements;


    public emof_Tag(
        String value,        String name    ) {
        super(
        );
        this.value = value;
        this.name = name;
        this.emof_elements = new ArrayList<>();
    }

    public emof_Tag(
        String value,        String name        ArrayList<emof_Element> emof_elements    ) {
        this.value = value;
        this.name = name;
        this.emof_elements = emof_elements;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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