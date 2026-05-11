





import java.util.List;
import java.util.ArrayList;

public class cmof_Tag extends Element {

    private String value;
    private String name;





    private List<cmof_Element> cmof_elements;


    public cmof_Tag(
        String value,        String name    ) {
        super(
        );
        this.value = value;
        this.name = name;
        this.cmof_elements = new ArrayList<>();
    }

    public cmof_Tag(
        String value,        String name        ArrayList<cmof_Element> cmof_elements    ) {
        this.value = value;
        this.name = name;
        this.cmof_elements = cmof_elements;
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

    public List<cmof_Element> getCmof_elements() {
        return cmof_elements;
    }

    public void addCmof_element(Cmof_element cmof_element) {
        this.cmof_elements.add(cmof_element);
    }

}