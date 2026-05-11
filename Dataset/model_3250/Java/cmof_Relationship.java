





import java.util.List;
import java.util.ArrayList;

public class cmof_Relationship extends Element {






    private List<cmof_Element> cmof_elements;


    public cmof_Relationship(
    ) {
        super(
        );
        this.cmof_elements = new ArrayList<>();
    }

    public cmof_Relationship(
        ArrayList<cmof_Element> cmof_elements    ) {
        this.cmof_elements = cmof_elements;
    }


    public List<cmof_Element> getCmof_elements() {
        return cmof_elements;
    }

    public void addCmof_element(Cmof_element cmof_element) {
        this.cmof_elements.add(cmof_element);
    }

}